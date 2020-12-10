from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import views 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('carrito/', views.carrito, name='carrito'),
    path('articulo/register/', staff_member_required(views.nuevoArticulo), name='articulo-register'),
    path('articulo/listar/', staff_member_required(views.ListarArticulosView.as_view()), name='articulo-listar'),
    path('articulo/modificar/<id>/', staff_member_required(views.modificarArticulo), name='articulo-modificar'),
    path('articulo/eliminar/<id>/', staff_member_required(views.eliminarArticulo), name='articulo-aliminar'),
    path('articulo/register/admin/', staff_member_required(views.RegistrarAdmin.as_view()), name='articulo-register-admin'),
    path('articulo/listar/usuarios/', staff_member_required(views.ListarUsuarios.as_view()), name='articulo-listar-usuarios'),
    path('articulo/eliminar/usuario/<str:email>/', staff_member_required(views.eliminarUsuario), name='articulo-eliminar-usuario')
    
]
