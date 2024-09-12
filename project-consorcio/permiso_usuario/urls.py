from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='permiso_usuario'),
    path('store/', views.store, name='store_permiso'),
     path('update/<int:id_permiso>/', views.update, name='update_permiso'),
    path('delete/<int:id_permiso>/', views.delete, name='delete_permiso'),
    path('show/<int:id_permiso>/', views.show, name='show_permiso'),
]