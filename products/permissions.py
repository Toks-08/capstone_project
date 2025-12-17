from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Read-only methods: allow anyone
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write methods: only allow admin users
        return request.user and request.user.is_staff
