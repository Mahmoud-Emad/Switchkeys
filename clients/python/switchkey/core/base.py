from typing import Any, Dict, List
from switchkey.api.types import (
    EnvironmentResponse,
    ProjectResponse,
    OrganizationResponse,
    UserResponse,
    ProjectUserResponse,
)
from switchkey.api.request import SwitchKeyRequest, SwitchKeyRequestMethod
from switchkey.core.exceptions import FeatureNotEnabled as FeatureNotEnabledError
from switchkey.api.routes import SwitchKeyRoutes, EndPoints


class SwitchKeyBase(type):
    pass


class SwitchKeyFeatures:
    def has(self, feature: str) -> bool:
        return True

    def get(self, feature: str) -> Any:
        pass

    def create(self, feature: str, value: str) -> None:
        pass

    def is_enabled(self, feature: str) -> bool:
        return False


class SwitchKey(metaclass=SwitchKeyBase):
    def __init__(self, environment_key: str) -> None:
        self.FeatureNotEnabled = FeatureNotEnabledError
        self.environment_key = environment_key
        self.features = SwitchKeyFeatures()
        self.__routes = SwitchKeyRoutes()
        self.environment_data = None
        self.environment = None

    def connect(self) -> None:
        environment = SwitchKeyRequest.call(
            self.__routes.get_route(EndPoints.ENVIRONMENTS_KEY, self.environment_key),
            SwitchKeyRequestMethod.GET,
        )
        self.environment_data = environment.data
        self.environment = self.__parse_environment()

    def __parse_device(self, device_data: Dict[str, Any]) -> None:
        pass

    def __parse_project_user(self, user_data: Dict[str, Any]) -> ProjectUserResponse:
        users = []
        for user in user_data:
            users.append(
                ProjectUserResponse(
                    device=self.__parse_device(user),
                    features=user.get("features"),
                    id=user.get("id"),
                    username=user.get("username"),
                )
            )
        return users

    def __parse_user(
        self, user_data: Dict[str, Any]
    ) -> UserResponse | List[UserResponse]:
        if type(user_data) == list:
            users: List[UserResponse] = []
            for user in user_data:
                users.append(
                    UserResponse(
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
            return UserResponse(
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
    ) -> OrganizationResponse:
        return OrganizationResponse(
            id=organization_data.get("id"),
            name=organization_data.get("name"),
            created=organization_data.get("created"),
            modified=organization_data.get("modified"),
            members=self.__parse_user(organization_data.get("members")),
            owner=self.__parse_user(organization_data.get("owner")),
        )

    def __parse_project(self, project_data: Dict[str, Any]) -> ProjectResponse:
        return ProjectResponse(
            id=project_data.get("id"),
            name=project_data.get("name"),
            created=project_data.get("created"),
            modified=project_data.get("modified"),
            organization=self.__parse_organization(project_data.get("organization")),
        )

    def __parse_environment(self) -> EnvironmentResponse:
        return EnvironmentResponse(
            created=self.environment_data.get("created"),
            id=self.environment_data.get("id"),
            project=self.__parse_project(self.environment_data.get("project")),
            environment_key=self.environment_data.get("environment_key"),
            modified=self.environment_data.get("modified"),
            name=self.environment_data.get("name"),
            users=self.__parse_project_user(self.environment_data.get("users")),
        )
