from django import forms
from django.forms import ModelForm
from .models import Articulo, Usuario

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

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        fields = ['nombreUsuario','telefono','email','sexo','contraseña','edad', 'img']

        widgets= {
            'nombreUsuario': forms.TextInput(
                attrs={
                    'id': 'registroNombre',
                    'class':'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'id': 'registroEmail',
                    'class':'form-control',
                    'placeholder': 'Ingrese su email'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'contraseña': forms.PasswordInput(
                attrs={
                    'id': 'registroPassword',
                    'class':'form-control',
                    'placeholder': 'Ingrese su email'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'id': 'registroTelefono',
                    'class':'form-control',
                    'placeholder': 'Ingrese número de telefono'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'id': 'registroEdad',
                    'class':'form-control',
                    'placeholder': 'Ingrese su edad',
                    'min': '24'
                }
            ),
            'img': forms.FileInput(
                attrs={
                    'class': 'custom-file-input',
                    'id': 'inputGroupFile01',
                    'aria-describedby': 'inputGroupFileAddon01'
                }
            )
        }