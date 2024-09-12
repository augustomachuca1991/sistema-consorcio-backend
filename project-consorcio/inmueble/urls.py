from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='inmueble'),
    path('store/', views.store, name='store_inmueble'),
    path('update/<int:id_inmueble>/', views.update, name='update_inmueble'),
    path('delete/<int:id_inmueble>/', views.delete, name='delete_inmueble'),
    path('show/<int:id_inmueble>/', views.show, name='show_inmueble'),
]