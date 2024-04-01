from switchkey.api.request.request import SwitchKeyRequest, SwitchKeyRequestMethod
from switchkey.api.request.types import UserTypeEnum
from switchkey.api.response.types import SwitchKeyAuthResponse
from switchkey.api.routes import EndPoints, SwitchKeyRoutes
from switchkey.core.exceptions import ResponseError
from switchkey.utils.parser import parse_auth
from switchkey.utils.config import SwitchKeyConfig


class SwitchKeyAuth:
    """
    Represents an API for managing auth.

    Methods:
    """

    def __init__(self):
        self.__routes = SwitchKeyRoutes()

    # @check_credentials()
    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        user_type: UserTypeEnum = UserTypeEnum.ADMINISTRATOR,
    ) -> SwitchKeyAuthResponse:
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

        user = parse_auth(user.data)
        access_token = user.access_token
        refresh_token = user.refresh_token

        config = SwitchKeyConfig()
        config.write(refresh_token=refresh_token, access_token=access_token)
        return user

    def login(self, email: str, password: str) -> SwitchKeyAuthResponse:
        """
        Method to login.

        Args:
            email (str): the user email.
            password (str): the user password.
        Raises:
            ResponseError: If there is an error while requesting.
        """

        data = {
            "email": email,
            "password": password,
        }
        
        url = self.__routes.get_route(EndPoints.LOGIN)
        user = SwitchKeyRequest.call(
            url=url,
            method=SwitchKeyRequestMethod.POST,
            data=data,
        )

        if user.error:
            raise ResponseError(user.error)

        elif user.error_message:
            raise ResponseError(user.error_message)

        user = parse_auth(user.data)
        access_token = user.access_token
        refresh_token = user.refresh_token

        config = SwitchKeyConfig()
        config.write(refresh_token=refresh_token, access_token=access_token)
        return user