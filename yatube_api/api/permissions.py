from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Проверка разрешений на небезопасные операции только авторам."""

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
