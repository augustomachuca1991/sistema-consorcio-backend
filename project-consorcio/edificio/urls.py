from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='edificio'),
    path('store/', views.store, name='store_edificio'),
    path('update/<int:id_edificio>/', views.update, name='update_edificio'),
]