from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='tipo_pago'),
    path('store/', views.store, name='store_tipo'),
     path('update/<int:id_tipo_pago>/', views.update, name='update_tipo'),
    path('delete/<int:id_tipo_pago>/', views.delete, name='delete_tipo'),
    path('<int:id_tipo_pago>/', views.show, name='show_tipo'), 

]