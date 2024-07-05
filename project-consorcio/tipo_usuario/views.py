from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tipo_usuario.models import TipoUsuario
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's TIPO DE USUARIO views")

#List of tipos de usuarios
def index(request):
    tipos_U = list(TipoUsuario.objects.all().values())
    return JsonResponse({"tipoUsuario": tipos_U})