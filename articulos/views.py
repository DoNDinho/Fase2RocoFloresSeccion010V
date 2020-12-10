from django.http import  HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 

from django.conf import settings
import os
import json
import requests

from .models import Articulo, Usuario
from .forms import ArticuloForm, UsuarioForm

class IndexView(generic.ListView):
    template_name = 'articulos/index.html'
    context_object_name = 'listaArticulos'

    def get_queryset(self):
        return Articulo.objects.all()

def about(request):
    return render(request, 'articulos/about.html')



@csrf_exempt
def register(request):
    data = {
        'form': UsuarioForm()  
    }

    if request.method =='POST':
        formulario= UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
            # Metodo para evitar el reenvio del formulario
            return HttpResponseRedirect(reverse('register'))
    else:
        return render(request, 'articulos/register.html', data)

        
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

            # Valida si el usuario está autenticado para enviar correo
            if request.user.is_authenticated:
                print(request.user.email)
                headers = {
                    'transaction_id': '1234556',
                    'timestamp': '2020-12-10T12:00:00',
                    'Content-Type': 'application/json',
                    'channel_id': '11',
                    'accept':'application/json'
                }

                body = {
                    "data": {
                        "token": {
                            "payload": {
                                "email": "test@gmail.com",
                                "password": "test123",
                                "nickname": "test user",
                                "age": 24,
                                "phone": "966206918"
                            }
                        }
                    }
                }

                r = requests.post('https://generateencrypttoken.azurewebsites.net/token/encrypt', headers=headers, json=body)
                print(r.status_code)
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


def login(request):
    return render(request, 'articulos/loginAdmin.html')


class RegistrarAdmin(generic.CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'articulos/registerAdmin.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            admin = Usuario(
                nombreUsuario = form.cleaned_data.get('nombreUsuario'),
                telefono = form.cleaned_data.get('telefono'),
                email = form.cleaned_data.get('email'),
                sexo = form.cleaned_data.get('sexo'),
                edad = form.cleaned_data.get('edad')
            )

            admin.set_password(form.cleaned_data.get('password'))
            admin.usuarioAdmin = True
            admin.save()
            return redirect('articulo-register-admin')
        else:
            return render(request, self.template_name, {'form': form})

class ListarUsuarios(generic.ListView):
    template_name = 'articulos/listarUsuarios.html'
    context_object_name = 'listaUsuarios'

    def get_queryset(self):
        return Usuario.objects.all()

def eliminarUsuario(request, email):
    usuario = Usuario.objects.get(email=email)
    
    # Valida si articulo posee imagen
    if usuario.img:
        # Eliminar imagen del directorio
        os.remove(str(settings.BASE_DIR) + usuario.img.url)
    
    usuario.delete()
    return redirect(to="articulo-listar-usuarios")