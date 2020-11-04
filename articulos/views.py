from django.http import  HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
# DESPUES ELIMINAR ESTO
from django.conf import settings
import os

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
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'articulos/register.html')

def carrito(request):
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
 
    return render(request, 'articulos/modificarArticulo.html', data)


def eliminarArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    
    # Valida si articulo posee imagen
    if articulo.img:
        # Eliminar imagen del directorio
        os.remove(str(settings.BASE_DIR) + articulo.img.url)
    
    articulo.delete()
    return redirect(to="articulo-listar")