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

    #class Habitante(models.Model):
    #id_habitante = models.AutoField(primary_key=True)
    #id_inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    #nombre = models.CharField(max_length=255)
    #dni = models.CharField(max_length=20)
    #correo = models.EmailField()
    #telefono = models.CharField(max_length=20)
    #created_at = models.DateTimeField(auto_now_add=True)

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

#metodo update para actualizar habitante
@csrf_exempt
def update(request, id_habitante):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'id_inmueble' not in data or 'nombre' not in data or 'dni' not in data or 'correo' not in data or 'telefono' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Obtener la instancia del habitante a actualizar
            habitante = Habitante.objects.get(pk=id_habitante)

            # Obtener la instancia de Inmueble usando el id recibido (porque es FK)
            id_inmueble = data['id_inmueble']
            inmueble = Inmueble.objects.get(pk=id_inmueble)

            # Actualizar los campos del habitante
            habitante.id_inmueble = inmueble
            habitante.nombre = data['nombre']
            habitante.dni = data['dni']
            habitante.correo = data['correo']
            habitante.telefono = data['telefono']
            habitante.save()

            return JsonResponse({'message': 'Habitante updated successfully'}, status=200)
        except Habitante.DoesNotExist:
            return JsonResponse({'error': 'Habitante not found'}, status=404)
        except Inmueble.DoesNotExist:
            return JsonResponse({'error': 'Inmueble not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

#borrar un registro de habitante
@csrf_exempt
def delete(request, id_habitante):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        habitante = Habitante.objects.get(id_habitante=id_habitante)
        habitante.delete()
        return JsonResponse({'message': 'Habitante deleted successfully'}, status=200)
    except Edificio.DoesNotExist:
        return JsonResponse({'error': 'Habitante not found'}, status=404)

#metodo mostrar, cuando presionamos show en el front
@csrf_exempt
def show(request, id_habitante):
    try:
        habitante = Habitante.objects.get(id_habitante=id_habitante)
        return JsonResponse({
            'id_habitante': habitante.id_habitante,
            'id_inmueble': habitante.id_inmueble,
            'nombre': habitante.nombre,
            'dni': habitante.dni,
            'correo': habitante.correo,
            'telefono': habitante.telefono,
            'created_at': habitante.created_at,
        })
    except Habitante.DoesNotExist:
        return JsonResponse({'error': 'Habitante not found'}, status=404)