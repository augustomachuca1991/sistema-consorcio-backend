from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from ingreso_cabecera.models import IngresoCabecera

import json

# Create your views here.
#List of tipos de pago
def index(request):
    cabecera = list(IngresoCabecera.objects.all().values())
    return JsonResponse({"cabecera": cabecera})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'total' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo tipo de pago
            new_cabecera = IngresoCabecera.objects.create(
                total=data['total']
             
            )
            return JsonResponse({'message': 'Cabecera created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
