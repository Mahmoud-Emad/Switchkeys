from switchkey.api.interfaces.response import SwitchKeyProjectResponse
from switchkey.api.request import SwitchKeyRequest, SwitchKeyRequestMethod
from switchkey.api.routes import EndPoints, SwitchKeyRoutes
from switchkey.core.exceptions import ResponseError
from switchkey.utils.parser import parse_project



class SwitchKeyProject:
    """
    Represents an API for managing projects.

    Methods:
        create(name: str, organization_id: int) -> SwitchKeyProjectResponse | ResponseError: Create a new organization.
    Args:
        api_token (Bearer Token):
            User token required only if you are going to make create/update/delete requests.
    """

    def __init__(self, api_token: str | None = None):
        self.api_token = api_token
        self.__routes = SwitchKeyRoutes()

    def create(self, organization_id: int, name: str) -> SwitchKeyProjectResponse | ResponseError:
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
        project = SwitchKeyRequest.call(
            url=url,
            method=SwitchKeyRequestMethod.POST,
            data=data,
            token=self.api_token,
        )

        if project.error_message:
            raise ResponseError(project.error_message)

        return parse_project(project.data)

    def update(self, new_organization_id: int, project_id: int, new_name: str) -> SwitchKeyProjectResponse | ResponseError:
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
        project = SwitchKeyRequest.call(
            url=url,
            method=SwitchKeyRequestMethod.PUT,
            data=data,
            token=self.api_token,
        )

        if project.error_message:
            raise ResponseError(project.error_message)

        return parse_project(project.data)

    def get(
        self, project_id: int
    ) -> SwitchKeyProjectResponse | ResponseError:
        """
        Method to get project.

        Args:
          project_id (int): the project ID.

        Raises:
          ResponseError: If there is an error while requesting.
        """

        url = self.__routes.get_route(EndPoints.PROJECTS_ID, project_id)
        project = SwitchKeyRequest.call(
            url=url,
            method=SwitchKeyRequestMethod.GET,
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
        project = SwitchKeyRequest.call(
            url=url, method=SwitchKeyRequestMethod.DELETE, token=self.api_token
        )

        if (
            project.error_message
            and project.error_message.lower() == "empty response content"
        ):
            return "Deleted"

        if project.error_message:
            raise ResponseError(project.error_message)

        return "Deleted"
