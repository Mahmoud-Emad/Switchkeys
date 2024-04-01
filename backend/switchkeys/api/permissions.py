from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from switchkeys.models.users import UserType


class UserIsAuthenticated(permissions.BasePermission):
    """
    logged in permission
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.is_authenticated and request.user.is_active:
            return True
        return False


class IsAdminUser(permissions.BasePermission):
    """
    check if the user is admin or not permission
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_active
            and request.user.user_type == UserType.ADMINISTRATOR
        )
