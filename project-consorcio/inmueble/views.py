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
