from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from edificio.models import Edificio
import json

# Create your views http
def index(resquest):
    return HttpResponse("Hello, it's Edificio section")
# list of edificios
def index(request):
    edificio = list(Edificio.objects.all().values())
    return JsonResponse({"edificio": edificio})