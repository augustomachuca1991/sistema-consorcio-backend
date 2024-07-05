from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's PERMISOS DE USUARIOS views")