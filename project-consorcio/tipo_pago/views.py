from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from tipo_pago.models import TipoPago

import json

# Create your views here.
#List of tipos de pago
def index(request):
    tipo = list(TipoPago.objects.all().values())
    return JsonResponse({"tipo": tipo})

@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validar datos
            if 'tipo' not in data:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Crear el nuevo tipo de pago
            new_tipoPago = TipoPago.objects.create(
                tipo=data['tipo']
             
            )
            return JsonResponse({'message': 'Tipo pago created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def update(request, id_topo_pago):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    try:
        tipo_pagp = TipoPago.objects.get(id_tipo_pago=id_id_tipo_pago)
    except TipoPago.DoesNotExist:
        return JsonResponse({'error': 'Tipo de Pago not found'}, status=404)
    
    # Actualizar los campos del usuario usando el método `update` de Django
    fields_to_update = {}
    for field in ['tipo']:
        if field in data:
            fields_to_update[field] = data[field]
    
    for field, value in fields_to_update.items():
        setattr(tipo_pago, field, value)
    tipo_pago.save()
    
    return JsonResponse({'message': 'Tipo de Pago updated successfully'}, status=200)

@csrf_exempt
def show(request, id_tipo_pago):
    try:
        tipo_pago = TipoPago.objects.get(id_tipo_pago=id_id_tipo_pago)
        return JsonResponse({
            'id_tipo_pago': tipo_pago.id_id_tipo_pago,
            'tipo': tipo_pago.tipo,
            'created_at': tipo_pago.created_at,
        })
    except TipoPago.DoesNotExist:
        return JsonResponse({'error': 'Tipo de Pago not found'}, status=404)

@csrf_exempt
def delete(request, id_id_tipo_pago):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        tipo_pago = TipoPago.objects.get(id_tipo_pago=id_id_tipo_pago)
        tipo_pago.delete()
        return JsonResponse({'message': 'Tipo de Pago deleted successfully'}, status=200)
    except TipoPago.DoesNotExist:
        return JsonResponse({'error': 'Tipo de Pago not found'}, status=404)
