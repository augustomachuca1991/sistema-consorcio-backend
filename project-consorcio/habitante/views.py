from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from habitante.models import Habitante
from inmueble.models import Inmueble
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's HABITANTE views")

#list of habitantes
def index(request):
    habitantes = list(Habitante.objects.all().values())
    return JsonResponse({"habitante": habitantes})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'id_inmueble' not in data or 'nombre' not in data or 'dni' not in data or 'correo' not in data or 'telefono' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Obtener instancia de Inmjueble usando el id recibido
            id_inmueble = data['id_inmueble']
            inmueble = Inmueble.objects.get(pk=id_inmueble)
            
            # Crear el nuevo usuario
            new_habitante = Habitante.objects.create(
                id_inmueble=inmueble,
                nombre=data['nombre'],
                dni=data['dni'],
                correo=data['correo'],
                telefono= data['telefono']
            )
            return JsonResponse({'message': 'Habitante created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
