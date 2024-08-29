from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    message = 'You do not have permission to delete this product.'

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated and request.user.is_superuser:
            return False
        return True
