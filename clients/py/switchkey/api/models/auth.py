from typing import Any, Dict, List

from switchkey.api.request.request import SwitchKeyRequest, SwitchKeyRequestMethod
from switchkey.api.request.types import UserTypeEnum
from switchkey.api.routes import EndPoints, SwitchKeyRoutes
from switchkey.core.exceptions import ResponseError
from switchkey.utils.parser import parse_auth


class SwitchKeyAuth:
    """
    Represents an API for managing auth.

    Methods:
    """

    def __init__(self):
        self.__routes = SwitchKeyRoutes()

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        user_type: UserTypeEnum = UserTypeEnum.ADMINISTRATOR,
    ):
        """
        Method to create a user.

        Args:
            first_name (str): the user first name.
            last_name (str): the user last name.
            email (str): the user email.
            password (str): the user password.
            user_type (UserTypeEnum.ADMINISTRATOR | UserTypeEnum.USER): the user password.
        Raises:
            ResponseError: If there is an error while requesting.
        """

        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "user_type": user_type,
        }

        url = self.__routes.get_route(EndPoints.SIGNUP)
        user = SwitchKeyRequest.call(
            url=url,
            method=SwitchKeyRequestMethod.POST,
            data=data,
        )

        if user.error:
            raise ResponseError(user.error)

        elif user.error_message:
            raise ResponseError(user.error_message)

        return parse_auth(user.data)
