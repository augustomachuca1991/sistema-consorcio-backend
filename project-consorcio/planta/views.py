from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from planta.models import Planta
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's PLANTA views")
    #List of tipos de planta
def index(request):
    planta = list(Planta.objects.all().values())
    return JsonResponse({"planta": planta})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'descripcion_planta' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo tipo de pago
            new_planta = Planta.objects.create(
                descripcion_planta=data['descripcion_planta']
             
            )
            return JsonResponse({'message': 'Planta created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

