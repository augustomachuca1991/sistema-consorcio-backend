"""
URL configuration for consorcio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView
from consorcio.views import MyTokenObtainPairView


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('polls/' , include('polls.urls')),
    path('api/users/' , include('users.urls')),
    path('ingresoCab/' , include('ingreso_cabecera.urls')),
    path('ingresoDet/' , include('ingreso_detalle.urls')),
    path('tipoPago/' , include('tipo_pago.urls')),
    path('seccion/', include('seccion.urls')),
    path('planta/', include('planta.urls')),
    
   
     path('planta/', include('planta.urls')),
    path('tipoUsuario/', include('tipo_usuario.urls')),
    path('permisos/', include('permiso_usuario.urls')),
    
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/edificios/', include('edificio.urls')),
    path('api/inmuebles/', include('inmueble.urls')),
    path('api/gastos/', include('gasto.urls')),
    path('api/habitantes/', include('habitante.urls')),
    path('api/cabecera/', include('cabecera.urls')),
    path('api/detalle/', include('detalle.urls')),



]
