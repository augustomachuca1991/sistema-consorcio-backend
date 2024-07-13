from django.http import JsonResponse
from django.contrib.auth.models import User

#List of users
def index(request):
    users = list(User.objects.all().values())
    return JsonResponse({"users": users})
