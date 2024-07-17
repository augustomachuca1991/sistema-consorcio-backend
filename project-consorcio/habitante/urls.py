from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='habitante'),
    path('store/', views.store, name='store_habitante'),
]