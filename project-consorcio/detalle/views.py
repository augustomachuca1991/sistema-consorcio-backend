from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from detalle.models import Detalle
from cabecera.models import Cabecera
from gasto.models import Gasto
import json


# list of edificios
def index(request):
    detalle = list(Detalle.objects.all().values())
    return JsonResponse({"detalle": detalle})


@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'id_cabecera' not in data or 'id_gasto' not in data or 'importe' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Obtener instancia de Cabecera usando el id recibido
            id_cabecera = data['id_cabecera']
            cabecera = Cabecera.objects.get(pk=id_cabecera)

            # Obtener instancia de Gasto usando el id recibido
            id_gasto = data['id_gasto']
            gasto = Gasto.objects.get(pk=id_gasto)
            
            # Crear el nuevo Detalle
            new_detalle = Detalle.objects.create(
                id_cabecera=cabecera,
                id_gasto=gasto,
                importe=data['importe'] 
            )
            return JsonResponse({'message': 'Detalle created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def delete(request, id_detalle):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        detalle = Detalle.objects.get(id_detalle=id_detalle)
        detalle.delete()
        return JsonResponse({'message': 'detalle eliminado correctamente'}, status=200)
    except Detalle.DoesNotExist:
        return JsonResponse({'error': 'detalle not found'}, status=404)

#para mostrar registro
@csrf_exempt
def show(request, id_detalle):
    try:
        detalle = Detalle.objects.get(id_detalle=id_detalle)
        return JsonResponse({
            'id_detalle': detalle.id_detalle,
            'id_cabecera': detalle.id_cabecera,
            'id_gasto': detalle.id_gasto,
            'importe': detalle.importe,
            'created_at': detalle.created_at,
        })
    except Detalle.DoesNotExist:
        return JsonResponse({'error': 'Detalle not found'}, status=404)
