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


#Actualizar campos de Permiso_usuario
@csrf_exempt
def update(request, id_permiso):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    try:
        permiso = PermisoUsuario.objects.get(id_permiso=id_permiso)
    except PermisoUsuario.DoesNotExist:
        return JsonResponse({'error': 'Permiso not found'}, status=404)
    
    # Actualizar los campos del permisos usando el método `update` de Django
    fields_to_update = {}
    for field in ['nombre']:
        if field in data:
            fields_to_update[field] = data[field]
    
    for field, value in fields_to_update.items():
        setattr(permiso, field, value)
        permiso.save()
    
    return JsonResponse({'message': 'Permiso updated successfully'}, status=200)

#borrado de permisos
@csrf_exempt
def delete(request, id_permiso):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        permiso = PermisoUsuario.objects.get(id_permiso=id_permiso)
        permiso.delete()
        return JsonResponse({'message': 'Permiso deleted successfully'}, status=200)
    except PermisoUsuario.DoesNotExist:
        return JsonResponse({'error': 'permiso not found'}, status=404)


#mostrar un registro

@csrf_exempt
def show(request, id_permiso):
    try:
        permiso = PermisoUsuario.objects.get(id_permiso=id_permiso)
        return JsonResponse({
            'id_permiso': permiso.id_permiso,
            'nombre': permiso.nombre,
            'created_at': permiso.created_at,
        })
    except PermisoUsuario.DoesNotExist:
        return JsonResponse({'error': 'Permiso not found'}, status=404)


