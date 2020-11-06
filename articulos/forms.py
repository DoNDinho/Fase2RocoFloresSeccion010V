from django import forms
from django.forms import ModelForm
from .models import Articulo

class ArticuloForm(ModelForm):
    class Meta:
        model= Articulo
        fields = ['tipoArticulo','nombre','precio','img','stock']
        
        widgets= {
            'tipoArticulo': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            )
        } 
       
 