from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='gasto'),
    path('store/', views.store, name='store_gasto'),
    path('update/<int:id_gasto>/', views.update, name='update_gasto'),
    path('delete/<int:id_gasto>/', views.delete, name='delete_gasto'),
    path('show/<int:id_gasto>/', views.show, name='show_gasto'),
    
]