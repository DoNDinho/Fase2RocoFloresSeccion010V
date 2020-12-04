from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('carrito/', views.carrito, name='carrito'),
    path('articulo/register/',login_required(views.nuevoArticulo), name='articulo-register'),
    path('articulo/listar/',login_required(views.ListarArticulosView.as_view()), name='articulo-listar'),
    path('articulo/modificar/<id>/',login_required(views.modificarArticulo), name='articulo-modificar'),
    path('articulo/eliminar/<id>/', login_required(views.eliminarArticulo), name='articulo-aliminar') 
]
