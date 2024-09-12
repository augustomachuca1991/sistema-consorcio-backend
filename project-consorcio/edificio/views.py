from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from edificio.models import Edificio
import json


# list of edificios
def index(request):
    edificio = list(Edificio.objects.all().values())
    return JsonResponse({"edificio": edificio})
    #Add new edificio
@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'nombre' not in data or 'direccion' not in data or 'telefono' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo usuario
            new_edificio = Edificio.objects.create(
                nombre=data['nombre'],
                direccion=data['direccion'],
                telefono=data['telefono']
            )
            return JsonResponse({'message': 'Edificio created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

#Actualizar Edificiio
@csrf_exempt
def update(request, id_edificio):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    try:
        edificio = Edificio.objects.get(id_edificio=id_edificio)
    except Edificio.DoesNotExist:
        return JsonResponse({'error': 'Edificio not found'}, status=404)
    
    # Actualizar los campos del usuario usando el método `update` de Django
    fields_to_update = {}
    for field in ['nombre', 'direccion', 'telefono']:
        if field in data:
            fields_to_update[field] = data[field]
    
    for field, value in fields_to_update.items():
        setattr(edificio, field, value)
    edificio.save()
    
    return JsonResponse({'message': 'Edificio updated successfully'}, status=200)

@csrf_exempt
def show(request, id_edificio):
    try:
        edificio = Edificio.objects.get(id_edificio=id_edificio)
        return JsonResponse({
            'id_edificio': edificio.id_edificio,
            'nombre': edificio.nombre,
            'direccion': edificio.direccion,
            'telefono': edificio.telefono,
            'created_at': edificio.created_at,
        })
    except Edificio.DoesNotExist:
        return JsonResponse({'error': 'Edificio not found'}, status=404)

@csrf_exempt
def delete(request, id_edificio):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        edificio = Edificio.objects.get(id_edificio=id_edificio)
        edificio.delete()
        return JsonResponse({'message': 'Edificio deleted successfully'}, status=200)
    except Edificio.DoesNotExist:
        return JsonResponse({'error': 'Edificio not found'}, status=404)