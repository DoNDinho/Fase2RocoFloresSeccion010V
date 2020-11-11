from django.contrib import admin

from .models import Tipo_Articulo, Articulo, Sexo, Usuario
from django.utils.html import format_html

class PersonArticulo(admin.ModelAdmin):
    list_display =(
        'tipoArticulo',
        'nombre',
        'precio',
        'img',
        'foto',
        'stock',
    )

    def foto(self, obj):
        return format_html("<img src={} />", obj.img.url )
    
admin.site.register(Tipo_Articulo)
admin.site.register(Articulo, PersonArticulo)
admin.site.register(Sexo)
admin.site.register(Usuario)


