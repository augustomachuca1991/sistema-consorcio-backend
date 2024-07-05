from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from habitante.models import Habitante
from inmueble.models import Inmueble
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's HABITANTE views")

#list of habitantes
def index(request):
    habitantes = list(Habitante.objects.all().values())
    return JsonResponse({"habitante": habitantes})