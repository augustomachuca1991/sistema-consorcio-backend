from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from gasto.models import Gasto
from django.db.models import Q
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello, it's GASTOS views")

# Vista para listar gastos y permitir búsqueda por término
def index(request):
    # Obtener el término de búsqueda desde los parámetros de la URL
    search_term = request.GET.get('search', '')

    # Filtrar si se cargó un término de búsqueda
    if search_term:
        gastos = Gasto.objects.filter(
            Q(descripcion_gasto__icontains=search_term)  # Filtra por descripción del gasto
        ).values()  # Asegúrate de convertir en un iterable
    else:
        # Si no hay término de búsqueda, devuelve todos los gastos
        gastos = Gasto.objects.all().values()  # No necesitas convertir a lista aquí
    # Convertir a lista antes de devolver la respuesta
    return JsonResponse({"gastos": list(gastos)}, safe=False)

#add new gasto
@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'descripcion_gasto' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo gasto
            new_gasto = Gasto.objects.create(
                descripcion_gasto=data['descripcion_gasto'],
                importe=data['importe']
            )
            return JsonResponse({'message': 'Gasto created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

#Update Gasto
@csrf_exempt
def update(request, id_gasto):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    try:
        gasto = Gasto.objects.get(id_gasto=id_gasto)
    except Gasto.DoesNotExist:
        return JsonResponse({'error': 'Gasto not found'}, status=404)
    
    # Actualizar los campos del gastos usando el método `update` de Django
    fields_to_update = {}
    for field in ['descripcion_gasto', 'importe']:
        if field in data:
            fields_to_update[field] = data[field]
    
    for field, value in fields_to_update.items():
        setattr(gasto, field, value)
    gasto.save()
    
    return JsonResponse({'message': 'Gasto updated successfully'}, status=200)

#Eliminar un registro de Gasto
@csrf_exempt
def delete(request, id_gasto):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        gasto = Gasto.objects.get(id_gasto=id_gasto)
        gasto.delete()
        return JsonResponse({'message': 'Gasto deleted successfully'}, status=200)
    except Gasto.DoesNotExist:
        return JsonResponse({'error': 'Gasto not found'}, status=404)


@csrf_exempt
def show(request, id_gasto):
    try:
        gasto = Gasto.objects.get(id_gasto=id_gasto)
        return JsonResponse({
            'id_gasto': gasto.id_gasto,
            'descripcion_gasto': gasto.descripcion_gasto,
            'importe': gasto.importe,
            'created_at': gasto.created_at,
        })
    except Gasto.DoesNotExist:
        return JsonResponse({'error': 'Gasto not found'}, status=404)