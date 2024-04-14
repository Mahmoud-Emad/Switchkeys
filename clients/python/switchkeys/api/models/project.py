from switchkeys.api.response.types import SwitchKeysProjectResponse
from switchkeys.api.request.request import SwitchKeysRequest, SwitchKeysRequestMethod
from switchkeys.api.routes import EndPoints, SwitchKeysRoutes
from switchkeys.core.exceptions import ResponseError
from switchkeys.utils.parser import parse_project



class SwitchKeysProject:
    """
    Represents an API for managing projects.

    Methods:
        create(name: str, organization_id: int) -> SwitchKeysProjectResponse | ResponseError: Create a new organization.
    Args:
        api_token (Bearer Token):
            User token required only if you are going to make create/update/delete requests.
    """

    def __init__(self, api_token: str | None = None):
        self.api_token = api_token
        self.__routes = SwitchKeysRoutes()

    def create(self, organization_id: int, name: str) -> SwitchKeysProjectResponse | ResponseError:
        """
        Method to create a project.

        Args:
            organization_id (int): the organization ID.
            name (str): The project name.

        Raises:
            ResponseError: If there is an error while requesting.
        """

        data = {"name": name, "organization_id": organization_id}

        url = self.__routes.get_route(EndPoints.PROJECTS)
        project = SwitchKeysRequest.call(
            url=url,
            method=SwitchKeysRequestMethod.POST,
            data=data,
            token=self.api_token,
        )

        if project.error_message:
            raise ResponseError(project.error_message)

        return parse_project(project.data)

    def update(self, new_organization_id: int, project_id: int, new_name: str) -> SwitchKeysProjectResponse | ResponseError:
        """
        Method to update a project.

        Args:
            new_organization_id (int): the organization ID.
            project_id (int): the project ID.
            new_name (str): The project name.

        Raises:
            ResponseError: If there is an error while requesting.
        """

        data = {"name": new_name, "organization_id": new_organization_id}

        url = self.__routes.get_route(EndPoints.PROJECTS_ID, project_id)
        project = SwitchKeysRequest.call(
            url=url,
            method=SwitchKeysRequestMethod.PUT,
            data=data,
            token=self.api_token,
        )

        if project.error_message:
            raise ResponseError(project.error_message)

        return parse_project(project.data)

    def get(
        self, project_id: int
    ) -> SwitchKeysProjectResponse | ResponseError:
        """
        Method to get project.

        Args:
          project_id (int): the project ID.

        Raises:
          ResponseError: If there is an error while requesting.
        """

        url = self.__routes.get_route(EndPoints.PROJECTS_ID, project_id)
        project = SwitchKeysRequest.call(
            url=url,
            method=SwitchKeysRequestMethod.GET,
        )

        if project.error_message:
            raise ResponseError(project.error_message)

        return parse_project(project.data)

    def delete(self, project_id: int) -> str | ResponseError:
        """
        Method to delete an project.

        Args:
          project_id (int): the project ID.

        Raises:
          ConnectionError: If there is an error while requesting.
        """

        url = self.__routes.get_route(EndPoints.PROJECTS_ID, project_id)
        project = SwitchKeysRequest.call(
            url=url, method=SwitchKeysRequestMethod.DELETE, token=self.api_token
        )

        if (
            project.error_message
            and project.error_message.lower() == "empty response content"
        ):
            return "Deleted"

        if project.error_message:
            raise ResponseError(project.error_message)

        return "Deleted"
