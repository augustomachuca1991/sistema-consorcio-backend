from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name= 'tipo_usuario'),
    path('store/', views.store, name='store_tipoUsuario'),
]