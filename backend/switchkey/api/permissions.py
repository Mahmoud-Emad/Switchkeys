from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class UserIsAuthenticated(permissions.BasePermission):
    """
    logged in permission
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.is_authenticated and request.user.is_active:
            return True
        return False
