from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from seccion.models import Seccion
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's SECCION views")

def index(request):
    seccion = list(Seccion.objects.all().values())
    return JsonResponse({"seccion": seccion})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'descripcion_seccion' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo tipo de pago
            new_seccion = Seccion.objects.create(
                descripcion_seccion=data['descripcion_seccion']
             
            )
            return JsonResponse({'message': 'Seccion created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

