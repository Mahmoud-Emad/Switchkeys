from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from switchkeys.api.permissions import (
    IsAdminUser,
    UserIsAuthenticated,
)
from switchkeys.api.custom_response import CustomResponse
from switchkeys.serializers.users import OrganizationUserSerializer
from switchkeys.services.users import get_user_by_email, get_user_by_id, get_all_users


class BaseGeneralUserAPIView(ListAPIView, GenericAPIView):
    permission_classes = []
    serializer_class = OrganizationUserSerializer

    def get_permissions(self):
        if self.request.method != "GET":
            self.permission_classes = [
                IsAdminUser,
            ]

        return super(BaseGeneralUserAPIView, self).get_permissions()

    def get_queryset(self) -> Response:
        """get all users in the system for a normal user"""
        query_set = get_all_users()
        return query_set


class GeneralUserAPIView(GenericAPIView):
    permission_classes = []
    serializer_class = OrganizationUserSerializer

    def get_permissions(self):
        if self.request.method != "GET":
            self.permission_classes = [
                IsAdminUser,
            ]

        return super(GeneralUserAPIView, self).get_permissions()

    def get(self, request: Request, id: str) -> Response:
        """To get a user by id"""
        user = get_user_by_id(id)
        if user is not None:
            return CustomResponse.success(
                data=self.get_serializer(user).data,
                message="User found",
                status_code=200,
            )
        return CustomResponse.not_found(message="User not found", status_code=404)

class GetUserByEmailAPIView(GenericAPIView):
    permission_classes = []
    serializer_class = OrganizationUserSerializer

    def get(self, request: Request, email: str) -> Response:
        """To get a user by id"""
        user = get_user_by_email(email)
        if user is not None:
            return CustomResponse.success(
                data=self.get_serializer(user).data,
                message="User found",
                status_code=200,
            )
        return CustomResponse.not_found(message="User not found", status_code=404)
