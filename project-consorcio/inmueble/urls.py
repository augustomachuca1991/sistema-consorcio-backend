from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='inmueble'),
    path('store/', views.store, name='store_inmueble'),
    
]