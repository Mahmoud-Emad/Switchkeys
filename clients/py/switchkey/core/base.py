from typing import Any, Dict, List
from uuid import UUID
from switchkey.api.models.auth import SwitchKeyAuth
from switchkey.api.models.organization import SwitchKeyOrganization
from switchkey.api.models.project import SwitchKeyProject
from switchkey.api.types import (
    SwitchKeyEnvironmentType,
    # SwitchKeyProjectType,
    # SwitchKeyOrganizationResponseType,
    # SwitchKeyUserType,
    SwitchKeyProjectUserType,
)
from switchkey.api.request.request import SwitchKeyRequest, SwitchKeyRequestMethod
from switchkey.core.exceptions import FeatureNotEnabled as FeatureNotEnabledError
from switchkey.api.routes import SwitchKeyRoutes, EndPoints


class SwitchKeyBase(type):
    """
    Metaclass for the SwitchKey class hierarchy.
    """

    pass


class SwitchKey(metaclass=SwitchKeyBase):
    """
    Represents the main SwitchKey class.

    Attributes:
        environment_key (str): The key of the environment.
        features (SwitchKeyFeatures): Features associated with the SwitchKey.
        __routes (SwitchKeyRoutes): Routes for the SwitchKey API.
        environment_data (dict): Data associated with the environment.
        environment (SwitchKeyEnvironmentType): Environment object.

    Methods:
        connect() -> None: Connect to the SwitchKey environment.
        __parse_device(device_data: Dict[str, Any]) -> None: Parse device data.
        __parse_project_user(user_data: Dict[str, Any]) -> SwitchKeyProjectUserType: Parse project user data.
        __parse_user(user_data: Dict[str, Any]) -> SwitchKeyUserType | List[SwitchKeyUserType]: Parse user data.
        __parse_organization(organization_data: Dict[str, Any]) -> SwitchKeyOrganizationResponseType: Parse organization data.
        __parse_project(project_data: Dict[str, Any]) -> SwitchKeyProjectType: Parse project data.
        __parse_environment() -> SwitchKeyEnvironmentType: Parse environment data.
    """

    def __init__(self, api_token: str | None = None) -> None:
        """
        Initialize the SwitchKey instance.

        Args:
            api_token (Bearer Token): User token required only if you are going to make create/update/delete requests.
        """

        self.api_token = api_token
        self.organization = SwitchKeyOrganization(api_token = self.api_token)
        self.project = SwitchKeyProject(api_token = self.api_token)
        self.auth = SwitchKeyAuth()

        self.FeatureNotEnabled = FeatureNotEnabledError
        self.features = {}
        self.__routes = SwitchKeyRoutes()
        self.environment_data = None
        self.environment = None
    
    def connect(self, environment_key: UUID) -> None:
        """
        Connect to the SwitchKey environment.

        Args:
            environment_key (UUID): The key of the environment to connect to.

        Raises:
            ConnectionError: If there is an error message in the response.

        Returns:
            None
        """
        self.environment_key = environment_key

        environment = SwitchKeyRequest.call(
            self.__routes.get_route(EndPoints.ENVIRONMENTS_KEY, self.environment_key),
            SwitchKeyRequestMethod.GET,
        )

        if environment.error_message:
            raise ConnectionError(environment.error_message)

        self.environment_data = environment.data
        self.environment = self.__parse_environment()

    def __parse_device(self, device_data: Dict[str, Any]) -> None:
        """
        Parse device data.

        Args:
            device_data (Dict[str, Any]): Device data to be parsed.
        """

        pass

    def __parse_project_user(
        self, user_data: Dict[str, Any]
    ) -> List[SwitchKeyProjectUserType]:
        """
        Parse project user data.

        Args:
            user_data (Dict[str, Any]): Project user data to be parsed.

        Returns:
            List[SwitchKeyProjectUserType]: Parsed project user object.
        """

        users = []
        for user in user_data:
            users.append(
                SwitchKeyProjectUserType(
                    device=self.__parse_device(user),
                    features=user.get("features"),
                    id=user.get("id"),
                    username=user.get("username"),
                    environment_key=self.environment_key
                )
            )
        return users


    def __parse_environment(self) -> SwitchKeyEnvironmentType:
        """
        Parse environment data.

        Returns:
            SwitchKeyEnvironmentType: Parsed environment object.
        """

        return SwitchKeyEnvironmentType(
            created=self.environment_data.get("created"),
            id=self.environment_data.get("id"),
            project=self.__parse_project(self.environment_data.get("project")),
            environment_key=self.environment_data.get("environment_key"),
            modified=self.environment_data.get("modified"),
            name=self.environment_data.get("name"),
            users=self.__parse_project_user(self.environment_data.get("users")),
        )
