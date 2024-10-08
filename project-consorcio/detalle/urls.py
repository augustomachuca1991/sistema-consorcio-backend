from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='detalle'),
    path('store/', views.store, name='store_detalle'),
    path('delete/<int:id_detalle>/', views.delete, name='delete_detalle'),
    path('show/<int:id_detalle>/', views.show, name='show_detalle'),
    
]