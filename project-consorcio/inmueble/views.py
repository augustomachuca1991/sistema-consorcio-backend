from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from edificio.models import Edificio
from inmueble.models import Inmueble
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's INMUEBLE views")

def index(resquest):
    inmueble = list(Inmueble.objects.all().values())
    return JsonResponse({"inmueble": inmueble})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'id_edificio' not in data or 'ubicacion' not in data or 'porcentaje' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Obtener instancia de Edificio usando el id recibido
            id_edificio = data['id_edificio']
            edificio = Edificio.objects.get(pk=id_edificio)
            
            # Crear el nuevo usuario
            new_inmueble = Inmueble.objects.create(
                id_edificio=edificio,
                ubicacion=data['ubicacion'],
                porcentaje=data['porcentaje']
            )
            return JsonResponse({'message': 'Inmueble created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

        #Update Edificiio
@csrf_exempt
def update(request, id_inmueble):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    try:
        inmueble = Inmueble.objects.get(id_inmueble=id_inmueble)
    except Inmueble.DoesNotExist:
        return JsonResponse({'error': 'Inmueble not found'}, status=404)
    
    # Actualizar los campos del usuario usando el método `update` de Django
    fields_to_update = {}
    for field in ['id_edificio', 'ubicacion', 'porcentaje']:
        if field in data:
            fields_to_update[field] = data[field]
    
    for field, value in fields_to_update.items():
        setattr(inmueble, field, value)
    inmueble.save()
    
    return JsonResponse({'message': 'Inmueble updated successfully'}, status=200)


@csrf_exempt
def delete(request, id_inmueble):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        inmueble = Inmueble.objects.get(id_inmueble=id_inmueble)
        inmueble.delete()
        return JsonResponse({'message': 'Inmueble deleted successfully'}, status=200)
    except Inmueble.DoesNotExist:
        return JsonResponse({'error': 'Inmueble not found'}, status=404)

#para mostrar registro
@csrf_exempt
def show(request, id_inmueble):
    try:
        inmueble = Inmueble.objects.get(id_inmueble=id_inmueble)
        return JsonResponse({
            'id_inmueble': inmueble.id_inmueble,
            'id_edificio': inmueble.id_edificio,
            'ubicacion': inmueble.ubicacion,
            'porcentaje': inmueble.porcentaje,
            'created_at': inmueble.created_at,
        })
    except Inmueble.DoesNotExist:
        return JsonResponse({'error': 'Inmueble not found'}, status=404)
