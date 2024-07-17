from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from permiso_usuario.models import PermisoUsuario

import json

# Create your views here.
def index(resquest):
    return HttpResponse("Hello, it's PERMISOS DE USUARIOS views")

    #list of habitantes
def index(request):
    permisos = list(PermisoUsuario.objects.all().values())
    return JsonResponse({"permisos": permisos})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'nombre' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo usuario
            new_permiso = PermisoUsuario.objects.create(
                
                nombre=data['nombre']
               
            )
            return JsonResponse({'message': 'Permiso created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
