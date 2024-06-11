from django.http import JsonResponse


def index(request):
    persons = [
        {'name': 'Pedro',
        'mail': 'pedro@hotmail.com'},
        {'name': 'Augusto',
        'mail': 'augusto@gamail.com'}
    ]
    return JsonResponse({"persons" : persons})