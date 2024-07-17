from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tipo_usuario.models import TipoUsuario
import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's TIPO DE USUARIO views")

#List of tipos de usuarios
def index(request):
    tipos_U = list(TipoUsuario.objects.all().values())
    return JsonResponse({"tipoUsuario": tipos_U})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'descripcion' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo tipo de pago
            new_tipoUsuario = TipoUsuario.objects.create(
                descripcion=data['descripcion']
             
            )
            return JsonResponse({'message': 'Tipo de Usuario created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)