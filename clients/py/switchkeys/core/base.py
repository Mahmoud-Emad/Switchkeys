from typing import Any, Dict, List
from uuid import UUID
from switchkeys.api.models.auth import SwitchKeysAuth
from switchkeys.api.models.organization import SwitchKeysOrganization
from switchkeys.api.models.project import SwitchKeysProject
from switchkeys.api.types import (
    SwitchKeysEnvironmentType,
    # SwitchKeysProjectType,
    # SwitchKeysOrganizationResponseType,
    # SwitchKeysUserType,
    SwitchKeysProjectUserType,
)
from switchkeys.api.request.request import SwitchKeysRequest, SwitchKeysRequestMethod
from switchkeys.core.exceptions import AuthenticationError, FeatureNotEnabled as FeatureNotEnabledError
from switchkeys.api.routes import SwitchKeysRoutes, EndPoints
from switchkeys.utils.config import SwitchKeysConfig
from switchkeys.utils.logger import SwitchKeysLogger


class SwitchKeysBase(type):
    """
    Metaclass for the SwitchKeys class hierarchy.
    """

    pass


class SwitchKeys(metaclass=SwitchKeysBase):
    """
    Represents the main SwitchKeys class.

    Attributes:
        environment_key (str): The key of the environment.
        features (SwitchKeysFeatures): Features associated with the SwitchKeys.
        __routes (SwitchKeysRoutes): Routes for the SwitchKeys API.
        environment_data (dict): Data associated with the environment.
        environment (SwitchKeysEnvironmentType): Environment object.

    Methods:
        connect() -> None: Connect to the SwitchKeys environment.
        __parse_device(device_data: Dict[str, Any]) -> None: Parse device data.
        __parse_project_user(user_data: Dict[str, Any]) -> SwitchKeysProjectUserType: Parse project user data.
        __parse_user(user_data: Dict[str, Any]) -> SwitchKeysUserType | List[SwitchKeysUserType]: Parse user data.
        __parse_organization(organization_data: Dict[str, Any]) -> SwitchKeysOrganizationResponseType: Parse organization data.
        __parse_project(project_data: Dict[str, Any]) -> SwitchKeysProjectType: Parse project data.
        __parse_environment() -> SwitchKeysEnvironmentType: Parse environment data.
    """

    def __init__(self, api_token: str | None = None) -> None:
        """
        Initialize the SwitchKeys instance.

        Args:
            api_token (Bearer Token): User token required only if you are going to make create/update/delete requests.
        """
        self.logger = SwitchKeysLogger.get_logger()
        self.auth = SwitchKeysAuth()

        if api_token is None:
            self.config = SwitchKeysConfig()
            if self.config.check():
                self.logger.info("The config file exists, and api_token is loaded from the config file.")
                self.api_token = self.config.load().access_token
        else:
            raise AuthenticationError("There are no tokens found in the config file, and none were specified when initializing an instance of the SwitchKeys client. Please ensure that tokens are provided either in the config file or passed during initialization.")

        self.api_token = api_token
        self.organization = SwitchKeysOrganization(api_token = self.api_token)
        self.project = SwitchKeysProject(api_token = self.api_token)

        # self.FeatureNotEnabled = FeatureNotEnabledError
        # self.features = {}
        # self.__routes = SwitchKeysRoutes()
        # self.environment_data = None
        # self.environment = None
    
    # def connect(self, environment_key: UUID) -> None:
    #     """
    #     Connect to the SwitchKeys environment.

    #     Args:
    #         environment_key (UUID): The key of the environment to connect to.

    #     Raises:
    #         ConnectionError: If there is an error message in the response.

    #     Returns:
    #         None
    #     """
    #     self.environment_key = environment_key

    #     environment = SwitchKeysRequest.call(
    #         self.__routes.get_route(EndPoints.ENVIRONMENTS_KEY, self.environment_key),
    #         SwitchKeysRequestMethod.GET,
    #     )

    #     if environment.error_message:
    #         raise ConnectionError(environment.error_message)

    #     self.environment_data = environment.data
    #     self.environment = self.__parse_environment()

    # def __parse_device(self, device_data: Dict[str, Any]) -> None:
    #     """
    #     Parse device data.

    #     Args:
    #         device_data (Dict[str, Any]): Device data to be parsed.
    #     """

    #     pass

    # def __parse_project_user(
    #     self, user_data: Dict[str, Any]
    # ) -> List[SwitchKeysProjectUserType]:
    #     """
    #     Parse project user data.

    #     Args:
    #         user_data (Dict[str, Any]): Project user data to be parsed.

    #     Returns:
    #         List[SwitchKeysProjectUserType]: Parsed project user object.
    #     """

    #     users = []
    #     for user in user_data:
    #         users.append(
    #             SwitchKeysProjectUserType(
    #                 device=self.__parse_device(user),
    #                 features=user.get("features"),
    #                 id=user.get("id"),
    #                 username=user.get("username"),
    #                 environment_key=self.environment_key
    #             )
    #         )
    #     return users


    # def __parse_environment(self) -> SwitchKeysEnvironmentType:
    #     """
    #     Parse environment data.

    #     Returns:
    #         SwitchKeysEnvironmentType: Parsed environment object.
    #     """

    #     return SwitchKeysEnvironmentType(
    #         created=self.environment_data.get("created"),
    #         id=self.environment_data.get("id"),
    #         project=self.__parse_project(self.environment_data.get("project")),
    #         environment_key=self.environment_data.get("environment_key"),
    #         modified=self.environment_data.get("modified"),
    #         name=self.environment_data.get("name"),
    #         users=self.__parse_project_user(self.environment_data.get("users")),
    #     )
