from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import action, permission_classes
from rest_framework import status
from .permissions import CanListUsers

#List of users
class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def list(self, request):
        users = list(User.objects.all().values())
        return JsonResponse({"users": users})

    @action(detail=False, methods=['post'])
    def addUser(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return JsonResponse({"error": "Username, password, and email are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({"message": "User created successfully", "user": {"id": user.id, "username": user.username, "email": user.email}}, status=status.HTTP_201_CREATED)

    
