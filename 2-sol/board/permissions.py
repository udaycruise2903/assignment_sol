from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to create/edit/delete data,
    but allow read-only access to any authenticated user.
    """

    def has_permission(self, request, view):
        if request.method in ['POST'] and not request.user.is_staff:
            return False
        return True


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
