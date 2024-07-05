from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
#from users.models import User
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's SECCION views")