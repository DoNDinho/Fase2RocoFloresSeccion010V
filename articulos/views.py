from django.shortcuts import render
from django.views import generic

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

def carrito(request):
    return render(request, 'articulos/carrito.html')

def nuevoArticulo(request):
    data ={
        'form':ArticuloForm()  
    }

    if request.method =='POST':
        formulario= ArticuloForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        data['mensaje'] = "guardado correctamente"
         
    return render(request, 'articulos/registerArticulo.html',data)

def modificarArticulo(request):
    data ={
        'form':ArticuloForm()  
    }

    return render(request, 'articulos/modificarArticulo.html',data)