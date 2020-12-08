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
        model = Usuario
        fields =  ['nombreUsuario','telefono','email','sexo','password','edad', 'img']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'id': 'registroEmail',
                    'class':'form-control',
                    'placeholder': 'Ingrese su email'
                }
            ),
            'nombreUsuario': forms.TextInput(
                attrs={
                    'id': 'registroNombre',
                    'class':'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'id': 'registroTelefono',
                    'class':'form-control',
                    'placeholder': 'Ingrese número de telefono'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'id': 'registroEdad',
                    'class':'form-control',
                    'placeholder': 'Ingrese su edad',
                    'min': '13'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'id': 'registroPassword',
                    'class':'form-control',
                    'placeholder': 'Ingrese su contraseña'
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

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user
