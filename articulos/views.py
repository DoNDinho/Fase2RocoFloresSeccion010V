from django.http import  HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
import os
import json

from .models import Articulo
from .forms import ArticuloForm

class IndexView(generic.ListView):
    template_name = 'articulos/index.html'
    context_object_name = 'listaArticulos'

    def get_queryset(self):
        return Articulo.objects.all()

def about(request):
    return render(request, 'articulos/about.html')


def register(request):
    return render(request, 'articulos/register.html')


@csrf_exempt
def carrito(request):
    if request.method == 'POST':
        # Lista que obtendra objeto con articulos modificados
        listaNuevoStock = []
        listaErrores =[]

        # El JSON serializado se convierte a formato JSON (Dict object)
        body = json.loads(request.body)

        # Recorremos el arreglo con articulos
        for articulos in body:
            id = articulos['id']
            cantidad = int(articulos['cantidad'])

            # Valida si existe objeto seleccionado
            try:
                articulo = Articulo.objects.get(id=id)
            except Articulo.DoesNotExist:
                print('Articulo no existe')

                error = {
                    'code': '001',
                    'message': 'Articulo no existe',
                    'id': id
                }

                listaErrores.append(error)

            else:
                print('Articulo existe')
                stock = articulo.stock

                # Valida si existe stock
                if stock == 0:
                    print('El producto no contiene stock')

                    error = {
                        'code': '002',
                        'message': 'Articulo sin stock',
                        'id': id
                    }

                    listaErrores.append(error)

                # Valida si la cantidad es mayor al stock
                elif cantidad > stock:
                    print('Stock insuficiente')

                    error = {
                        'code': '002',
                        'message': 'Stock insuficiente: ' + str(stock),
                        'id': id
                    }

                    listaErrores.append(error)
                else:
                    print('Stock suficiente')

        # Valida si la lista de errores contiene items
        if(len(listaErrores) > 0):
            
            # Responde la peticion con la lista de errores
            return JsonResponse({
                'errors': listaErrores
            })
        else:
            # Recorre lista con articulos para modificar stock
            for articulos in body:
                id = articulos['id']
                cantidad = int(articulos['cantidad'])

                articulo = Articulo.objects.get(id=id)
                articulo.stock = articulo.stock - cantidad
                articulo.save()

            return JsonResponse({})
   
    else:
        return render(request, 'articulos/carrito.html')


def nuevoArticulo(request):
    data ={
        'form':ArticuloForm()  
    }

    if request.method =='POST':
        formulario= ArticuloForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
            # Metodo para evitar el reenvio del formulario
            return HttpResponseRedirect(reverse('articulo-register'))
    else:
        return render(request, 'articulos/registerArticulo.html',data)


class ListarArticulosView(generic.ListView):
    template_name = 'articulos/listarArticulos.html'
    context_object_name = 'listaArticulos'

    def get_queryset(self):
        return Articulo.objects.all()

def modificarArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    data ={
        'form':ArticuloForm(instance=articulo)  
    }

    if request.method =='POST':
        formulario= ArticuloForm(data=request.POST, instance=articulo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
            data['form'] = formulario
        data['form'] = ArticuloForm(instance=Articulo.objects.get(id=id))
        
    return render(request, 'articulos/registerArticulo.html', data)


def eliminarArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    
    # Valida si articulo posee imagen
    if articulo.img:
        # Eliminar imagen del directorio
        os.remove(str(settings.BASE_DIR) + articulo.img.url)
    
    articulo.delete()
    return redirect(to="articulo-listar")