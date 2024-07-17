from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from gasto.models import Gasto
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's GASTOS views")
#list of gastos
def index(request):
    gastos = list(Gasto.objects.all().values())
    return JsonResponse({"gastos": gastos})
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
                descripcion_gasto=data['descripcion_gasto']
              
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
    
    # Actualizar los campos del usuario usando el método `update` de Django
    fields_to_update = {}
    for field in ['descripcion_gasto']:
        if field in data:
            fields_to_update[field] = data[field]
    
    for field, value in fields_to_update.items():
        setattr(gasto, field, value)
    gasto.save()
    
    return JsonResponse({'message': 'Gasto updated successfully'}, status=200)

