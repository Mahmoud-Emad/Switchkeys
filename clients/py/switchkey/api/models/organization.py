from typing import List

from switchkey.api.response.types import (
    SwitchKeyOrganizationResponse,
    SwitchKeyUserResponse,
)
from switchkey.api.models.project import SwitchKeyProject
from switchkey.api.request.request import SwitchKeyRequest, SwitchKeyRequestMethod
from switchkey.api.routes import EndPoints, SwitchKeyRoutes
from switchkey.api.models.user import SwitchKeyUser
from switchkey.core.exceptions import ResponseError
from switchkey.utils.parser import parse_organization


class SwitchKeyOrganization:
    """
    Represents an API for managing organizations.

    Methods:
        create(name: str, members: List[SwitchKeyUserResponse] | None) -> SwitchKeyOrganizationResponse | ResponseError:
            Create a new organization.
        update(organization_id: int, new_name: str, new_members: List[SwitchKeyUserResponse] | None) -> SwitchKeyOrganizationResponse | ResponseError:
            Update an organization.
        delete(organization_id: int) -> str[`deleted`] | ResponseError:
            Delete an organization.
        get(organization_id: int) -> SwitchKeyOrganizationResponse | ResponseError:
            Retrieve an organization by ID.

    Args:
        api_token (Bearer Token):
            User token required only if you are going to make create/update/delete requests.
    """

    def __init__(self, api_token: str | None = None):
        self.api_token = api_token
        self.__routes = SwitchKeyRoutes()
        self.members = SwitchKeyUser()
        self.owner = SwitchKeyUser()
        self.projects = SwitchKeyProject(api_token=self.api_token)

    def create(
        self,
        name: str,
        members: List[SwitchKeyUserResponse] | None = None,
    ) -> SwitchKeyOrganizationResponse | ResponseError:
        """
        Method to create an organization.

        Args:
            name (str): the organization name.
            members (SwitchKeyUser | None): the organization members, can be a list of SwitchKeyUser or None.

        Raises:
            ResponseError: If there is an error while requesting.
        """

        data = {"name": name}
        if members is not None:
            data["members"] = members

        url = self.__routes.get_route(EndPoints.ORGANIZATIONS)
        organization = SwitchKeyRequest.call(
            url=url,
            method=SwitchKeyRequestMethod.POST,
            data=data,
            token=self.api_token,
        )

        if organization.error_message:
            raise ResponseError(organization.error_message)

        return parse_organization(organization.data)

    def update(
        self,
        organization_id: int,
        new_name: str,
        new_members: List[SwitchKeyUserResponse] | None = None,
    ) -> SwitchKeyOrganizationResponse | ResponseError:
        """
        Method to update an organization.

        Args:
          organization_id (int): the organization ID.
          new_name (str): the organization new name.
          new_members (SwitchKeyUser | None): the organization members, can be a list of SwitchKeyUser or None.

        Raises:
            ResponseError: If there is an error while requesting.
        """

        data = {"name": new_name}
        if new_members is not None:
            data["members"] = new_members

        url = self.__routes.get_route(EndPoints.ORGANIZATIONS_ID, organization_id)
        organization = SwitchKeyRequest.call(
            url=url,
            method=SwitchKeyRequestMethod.PUT,
            data=data,
            token=self.api_token,
        )

        if organization.error_message:
            raise ResponseError(organization.error_message)

        return parse_organization(organization.data)

    def get(
        self, organization_id: int
    ) -> SwitchKeyOrganizationResponse | ResponseError:
        """
        Method to get an organization.

        Args:
          organization_id (int): the organization ID.

        Raises:
          ResponseError: If there is an error while requesting.
        """

        url = self.__routes.get_route(EndPoints.ORGANIZATIONS_ID, organization_id)
        organization = SwitchKeyRequest.call(
            url=url,
            method=SwitchKeyRequestMethod.GET,
        )

        if organization.error_message:
            raise ResponseError(organization.error_message)

        return parse_organization(organization.data)

    def delete(self, organization_id: int) -> str | ResponseError:
        """
        Method to delete an organization.

        Args:
          organization_id (int): the organization ID.

        Raises:
          ConnectionError: If there is an error while requesting.
        """

        url = self.__routes.get_route(EndPoints.ORGANIZATIONS_ID, organization_id)
        organization = SwitchKeyRequest.call(
            url=url, method=SwitchKeyRequestMethod.DELETE, token=self.api_token
        )

        if (
            organization.error_message
            and organization.error_message.lower() == "empty response content"
        ):
            return "Deleted"

        if organization.error_message:
            raise ResponseError(organization.error_message)

        return "Deleted"
