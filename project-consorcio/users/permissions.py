from rest_framework import permissions


class CanListUsers(permissions.BasePermission):
    """
    Custom permission to only allow staff members to list users.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a staff member
        return request.user and request.user.is_authenticated and request.user.is_staff

class CanAddUser(permissions.BasePermission):
    """
    Custom permission to only allow staff members to add users.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a staff member
        return request.user and request.user.is_authenticated and request.user.is_staff