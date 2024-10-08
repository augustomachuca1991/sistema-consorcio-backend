from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='cabecera'),
    path('store/', views.store, name='store_cabecera'),
    path('delete/<int:id_cabecera>/', views.delete, name='delete_cabecera'),
    path('show/<int:id_cabecera>/', views.show, name='show_cabecera'),
    
]