from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='habitante'),
    path('store/', views.store, name='store_habitante'),
    path('update/<int:id_habitante>/', views.update, name='update_habitante'),
    path('delete/<int:id_habitante>/', views.delete, name='delete_habitante'),
    path('show/<int:id_habitante>/', views.show, name='show_habitante'),
]