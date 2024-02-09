from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False

    def has_permission(self, request, view):
        return request.user.is_superuser
