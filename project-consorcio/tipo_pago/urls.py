from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='tipo_pago'),
    path('store/', views.store, name='store_tipo'), 

]