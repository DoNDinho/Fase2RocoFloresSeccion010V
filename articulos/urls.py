from django.urls import path

from . import views 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('carrito/', views.carrito, name='carrito'),
    path('articulo/register', views.nuevoArticulo, name='articulo-register'),
    path('articulo/listar', views.ListarArticulosView.as_view(), name='articulo-listar'),
    path('articulo/modificar', views.modificarArticulo, name='articulo-modificar'),
    path('articulo/eliminar/<id>/', views.eliminarArticulo, name='articulo-aliminar')
]