from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff  # Only allow access to admin users

class IsProductManager(BasePermission):
    def has_permission(self, request, view):
        # Define logic for product manager
        return request.user.groups.filter(name='Product Manager').exists()

class IsProductOwner(BasePermission):
    def has_permission(self, request, view):
        # Define logic for product owner
        return request.user.groups.filter(name='Product Owner').exists()
