from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from cabecera.models import Cabecera
from habitante.models import Habitante
from inmueble.models import Inmueble
import json


# list of cabecera
def index(request):
    cabecera = list(Cabecera.objects.all().values())
    return JsonResponse({"cabecera": cabecera})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'id_habitante' not in data or 'id_inmueble' not in data or 'fecha' not in data or 'total_gastos' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Obtener instancia de Habitante usando el id recibido
            id_habitante = data['id_habitante']
            habitante = Habitante.objects.get(pk=id_habitante)

            # Obtener instancia de Inmueble usando el id recibido
            id_inmueble = data['id_inmueble']
            inmueble = Inmueble.objects.get(pk=id_inmueble)
            
            # Crear el nuevo Cabecera
            new_cabecera = Cabecera.objects.create(
                id_habitante=habitante,
                id_inmueble=inmueble,
                fecha=data['fecha'],
                total_gastos=data['total_gastos']

            )
            return JsonResponse({'message': 'Cabecera created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def delete(request, id_cabecera):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        cabecera = Cabecera.objects.get(id_cabecera=id_cabecera)
        cabecera.delete()
        return JsonResponse({'message': 'cabecera eliminada correctamente'}, status=200)
    except Cabecera.DoesNotExist:
        return JsonResponse({'error': 'Cabecera not found'}, status=404)

#para mostrar registro
@csrf_exempt
def show(request, id_cabecera):
    try:
        cabecera = Cabecera.objects.get(id_cabecera=id_cabecera)
        return JsonResponse({
            'id_habitante': cabecera.id_habitante,
            'id_inmueble': cabecera.id_inmueble,
            'fecha': cabecera.fecha,
            'total_gastos': cabecera.total_gastos,
            'created_at': cabecera.created_at,
        })
    except Cabecera.DoesNotExist:
        return JsonResponse({'error': 'cabecera not found'}, status=404)
