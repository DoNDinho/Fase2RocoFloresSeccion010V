from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('carrito', views.carrito, name='carrito'),
]