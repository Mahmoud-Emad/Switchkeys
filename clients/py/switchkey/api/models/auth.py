from switchkeys.api.request.request import SwitchKeysRequest, SwitchKeysRequestMethod
from switchkeys.api.request.types import UserTypeEnum
from switchkeys.api.response.types import SwitchKeysAuthResponse
from switchkeys.api.routes import EndPoints, SwitchKeysRoutes
from switchkeys.core.exceptions import ResponseError
from switchkeys.utils.parser import parse_auth
from switchkeys.utils.config import SwitchKeysConfig


class SwitchKeysAuth:
    """
    Represents an API for managing auth.

    Methods:
    """

    def __init__(self):
        self.__routes = SwitchKeysRoutes()

    # @check_credentials()
    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        user_type: UserTypeEnum = UserTypeEnum.ADMINISTRATOR,
    ) -> SwitchKeysAuthResponse:
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
        user = SwitchKeysRequest.call(
            url=url,
            method=SwitchKeysRequestMethod.POST,
            data=data,
        )

        if user.error:
            raise ResponseError(user.error)

        elif user.error_message:
            raise ResponseError(user.error_message)

        user = parse_auth(user.data)
        access_token = user.access_token
        refresh_token = user.refresh_token

        config = SwitchKeysConfig()
        config.write(refresh_token=refresh_token, access_token=access_token)
        return user

    def login(self, email: str, password: str) -> SwitchKeysAuthResponse:
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
        user = SwitchKeysRequest.call(
            url=url,
            method=SwitchKeysRequestMethod.POST,
            data=data,
        )

        if user.error:
            raise ResponseError(user.error)

        elif user.error_message:
            raise ResponseError(user.error_message)

        user = parse_auth(user.data)
        access_token = user.access_token
        refresh_token = user.refresh_token

        config = SwitchKeysConfig()
        config.write(refresh_token=refresh_token, access_token=access_token)
        return user