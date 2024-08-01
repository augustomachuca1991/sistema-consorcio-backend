from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.UserViewSet.as_view({'get': 'list'}), name='users'),
    path('store/', views.UserViewSet.as_view({'post': 'addUser'}), name='user_store')

]