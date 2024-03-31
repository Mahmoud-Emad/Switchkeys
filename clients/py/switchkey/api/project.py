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

    def create(self, organization_id: int, name: str):
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
