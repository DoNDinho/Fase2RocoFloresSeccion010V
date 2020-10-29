from django.shortcuts import render
from django.views import generic

from .models import Articulo

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