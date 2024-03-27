from typing import List
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from switchkey.models.users import User
from switchkey.api.permissions import (
    UserIsAuthenticated,
)
# from switchkey.api.custom_response import CustomResponse
from switchkey.serializers.users import GeneralUserSerializer
from switchkey.services.users import get_user_by_id, get_all_users


class BaseGeneralUserAPIView(ListAPIView, GenericAPIView):
    permission_classes = [UserIsAuthenticated]
    serializer_class = GeneralUserSerializer

    def get_queryset(self) -> Response:
        """get all users in the system for a normal user"""
        query_set = get_all_users()
        return query_set

