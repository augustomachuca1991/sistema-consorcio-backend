from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('store/', views.store, name='store_user'),
    path('update/<int:user_id>/', views.update, name='update_user'),
    path('show/<int:user_id>/', views.show, name='show_user'),
    path('destroy/<int:user_id>/', views.destroy, name='destroy_user'),

]