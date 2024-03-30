from enum import Enum

class EndPoints(Enum):
    """Enumeration of API endpoints."""
    # Endpoints without parameters
    CHANGE_PASSWORD = "http://127.0.0.1:8000/api/auth/change-password/"
    REFRESH_TOKEN = "http://127.0.0.1:8000/api/auth/token/refresh/"
    ORGANIZATIONS = "http://127.0.0.1:8000/api/organizations/"
    ENVIRONMENTS = "http://127.0.0.1:8000/api/environments/"
    PROJECTS = "http://127.0.0.1:8000/api/projects/"
    GROUPS = "http://127.0.0.1:8000/api/groups/"
    SIGNUP = "http://127.0.0.1:8000/api/auth/signup/"
    LOGIN = "http://127.0.0.1:8000/api/auth/login/"
    USERS = "http://127.0.0.1:8000/api/auth/users/"
    
    # Endpoints with parameters
    ORGANIZATIONS_ID = "http://127.0.0.1:8000/api/organizations/{}/"
    ENVIRONMENTS_KEY = "http://127.0.0.1:8000/api/environments/key/{}/"
    ENVIRONMENTS_SET = "http://127.0.0.1:8000/api/environments/key/{}/set/?user_id={}"
    ENVIRONMENTS_ID = "http://127.0.0.1:8000/api/environments/{}/"
    PROJECTS_ID = "http://127.0.0.1:8000/api/projects/{}/"
    GROUPS_ID = "http://127.0.0.1:8000/api/groups/{}/"
    USERS_ID = "http://127.0.0.1:8000/api/auth/users/{}/"

class SwitchKeyRoutes:
    """Class to manage API routes."""

    def __init__(self) -> None:
        """Initialize the SwitchKeyRoutes instance."""
        self.endpoints = EndPoints

    def get_route(self, endpoint: EndPoints, *args) -> str:
        """
        Get the URL for the specified endpoint.

        Args:
            endpoint (EndPoints): The endpoint for which to get the URL.
            args: Optional arguments to be inserted into the URL if needed.

        Returns:
            str: The URL for the specified endpoint.
        """
        if endpoint in [EndPoints.ORGANIZATIONS_ID, EndPoints.ENVIRONMENTS_KEY, EndPoints.ENVIRONMENTS_SET,
                        EndPoints.ENVIRONMENTS_ID, EndPoints.PROJECTS_ID,
                        EndPoints.GROUPS_ID, EndPoints.USERS_ID]:
            return endpoint.value.format(*args)
        else:
            return endpoint.value
