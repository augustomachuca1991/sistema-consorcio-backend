from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from gasto.models import Gasto
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's GASTOS views")
#list of gastos
def index(request):
    gastos = list(Gasto.objects.all().values())
    return JsonResponse({"gastos": gastos})
