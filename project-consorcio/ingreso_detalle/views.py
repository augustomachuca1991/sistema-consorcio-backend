from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from ingreso_detalle.models import IngresoDetalle

import json

# Create your views here.
#List of tipos de pago
def index(request):
    detalle = list(IngresoDetalle.objects.all().values())
    return JsonResponse({"detalle": detalle})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'concepto' not in data or 'descripcion' not in data or 'saldo' not in data or 'id_tipo_pago' not in data or 'id_ingreso_cabecera' not in data or 'importe' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo tipo de pago
            new_detalle = IngresoDetalle.objects.create(
                concepto=data['concepto'],
                descripcion=data['descripcion'],
                saldo=data['saldo'],
                id_tipo_pago=data['id_tipo_pago'],
                id_ingreso_cabecera=data['id_ingreso_cabecera'],
                importe=data['importe']
             
            )
            return JsonResponse({'message': 'Detalle created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
