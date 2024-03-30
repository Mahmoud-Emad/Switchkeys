from typing import Any, Dict, List
from uuid import UUID
from switchkey.api.types import (
    SwitchKeyEnvironmentType,
    SwitchKeyProjectType,
    SwitchKeyOrganizationType,
    SwitchKeyUserType,
    SwitchKeyProjectUserType,
)
from switchkey.api.request import SwitchKeyRequest, SwitchKeyRequestMethod
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
        __parse_organization(organization_data: Dict[str, Any]) -> SwitchKeyOrganizationType: Parse organization data.
        __parse_project(project_data: Dict[str, Any]) -> SwitchKeyProjectType: Parse project data.
        __parse_environment() -> SwitchKeyEnvironmentType: Parse environment data.
    """

    def __init__(self, environment_key: UUID) -> None:
        """
        Initialize the SwitchKey instance.

        Args:
            environment_key (uuid): The key of the environment.
        """

        self.FeatureNotEnabled = FeatureNotEnabledError
        self.environment_key = environment_key
        self.features = {}
        self.__routes = SwitchKeyRoutes()
        self.environment_data = None
        self.environment = None
    
    def connect(self) -> None:
        """
        Connect to the SwitchKey environment.
        """

        environment = SwitchKeyRequest.call(
            self.__routes.get_route(EndPoints.ENVIRONMENTS_KEY, self.environment_key),
            SwitchKeyRequestMethod.GET,
        )

        if environment.error_message is not None:
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

    def __parse_user(
        self, user_data: Dict[str, Any]
    ) -> SwitchKeyUserType | List[SwitchKeyUserType]:
        """
        Parse user data.

        Args:
            user_data (Dict[str, Any]): User data to be parsed.

        Returns:
            SwitchKeyUserType | List[SwitchKeyUserType]: Parsed user object or list of parsed user objects.
        """

        if type(user_data) == list:
            users: List[SwitchKeyUserType] = []
            for user in user_data:
                users.append(
                    SwitchKeyUserType(
                        background_color=user.get("background_color"),
                        email=user.get("email"),
                        first_name=user.get("first_name"),
                        full_name=user.get("full_name"),
                        is_active=user.get("is_active"),
                        id=user.get("id"),
                        joining_at=user.get("joining_at"),
                        last_name=user.get("last_name"),
                    )
                )
        else:
            return SwitchKeyUserType(
                background_color=user_data.get("background_color"),
                email=user_data.get("email"),
                first_name=user_data.get("first_name"),
                full_name=user_data.get("full_name"),
                is_active=user_data.get("is_active"),
                id=user_data.get("id"),
                joining_at=user_data.get("joining_at"),
                last_name=user_data.get("last_name"),
            )

    def __parse_organization(
        self, organization_data: Dict[str, Any]
    ) -> SwitchKeyOrganizationType:
        """
        Parse organization data.

        Args:
            organization_data (Dict[str, Any]): Organization data to be parsed.

        Returns:
            SwitchKeyOrganizationType: Parsed organization object.
        """

        return SwitchKeyOrganizationType(
            id=organization_data.get("id"),
            name=organization_data.get("name"),
            created=organization_data.get("created"),
            modified=organization_data.get("modified"),
            members=self.__parse_user(organization_data.get("members")),
            owner=self.__parse_user(organization_data.get("owner")),
        )

    def __parse_project(self, project_data: Dict[str, Any]) -> SwitchKeyProjectType:
        """
        Parse project data.

        Args:
            project_data (Dict[str, Any]): Project data to be parsed.

        Returns:
            SwitchKeyProjectType: Parsed project object.
        """

        return SwitchKeyProjectType(
            id=project_data.get("id"),
            name=project_data.get("name"),
            created=project_data.get("created"),
            modified=project_data.get("modified"),
            organization=self.__parse_organization(project_data.get("organization")),
        )

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
