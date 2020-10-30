from django import forms
from django.forms import ModelForm
from .models import Articulo

class ArticuloForm(ModelForm):
    class Meta:
        model= Articulo
        fields = ['tipoArticulo','nombre','precio','img','stock']
        


 