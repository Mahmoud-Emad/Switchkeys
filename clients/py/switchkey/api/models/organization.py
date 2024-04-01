from typing import List

from switchkeys.api.response.types import (
    SwitchKeysOrganizationResponse,
    SwitchKeysUserResponse,
)
from switchkeys.api.models.project import SwitchKeysProject
from switchkeys.api.request.request import SwitchKeysRequest, SwitchKeysRequestMethod
from switchkeys.api.routes import EndPoints, SwitchKeysRoutes
from switchkeys.api.models.user import SwitchKeysUser
from switchkeys.core.exceptions import ResponseError
from switchkeys.utils.parser import parse_organization


class SwitchKeysOrganization:
    """
    Represents an API for managing organizations.

    Methods:
        create(name: str, members: List[SwitchKeysUserResponse] | None) -> SwitchKeysOrganizationResponse | ResponseError:
            Create a new organization.
        update(organization_id: int, new_name: str, new_members: List[SwitchKeysUserResponse] | None) -> SwitchKeysOrganizationResponse | ResponseError:
            Update an organization.
        delete(organization_id: int) -> str[`deleted`] | ResponseError:
            Delete an organization.
        get(organization_id: int) -> SwitchKeysOrganizationResponse | ResponseError:
            Retrieve an organization by ID.

    Args:
        api_token (Bearer Token):
            User token required only if you are going to make create/update/delete requests.
    """

    def __init__(self, api_token: str | None = None):
        self.api_token = api_token
        self.__routes = SwitchKeysRoutes()
        self.members = SwitchKeysUser()
        self.owner = SwitchKeysUser()
        self.projects = SwitchKeysProject(api_token=self.api_token)

    def create(
        self,
        name: str,
        members: List[SwitchKeysUserResponse] | None = None,
    ) -> SwitchKeysOrganizationResponse | ResponseError:
        """
        Method to create an organization.

        Args:
            name (str): the organization name.
            members (SwitchKeysUser | None): the organization members, can be a list of SwitchKeysUser or None.

        Raises:
            ResponseError: If there is an error while requesting.
        """

        data = {"name": name}
        if members is not None:
            data["members"] = members

        url = self.__routes.get_route(EndPoints.ORGANIZATIONS)
        organization = SwitchKeysRequest.call(
            url=url,
            method=SwitchKeysRequestMethod.POST,
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
        new_members: List[SwitchKeysUserResponse] | None = None,
    ) -> SwitchKeysOrganizationResponse | ResponseError:
        """
        Method to update an organization.

        Args:
          organization_id (int): the organization ID.
          new_name (str): the organization new name.
          new_members (SwitchKeysUser | None): the organization members, can be a list of SwitchKeysUser or None.

        Raises:
            ResponseError: If there is an error while requesting.
        """

        data = {"name": new_name}
        if new_members is not None:
            data["members"] = new_members

        url = self.__routes.get_route(EndPoints.ORGANIZATIONS_ID, organization_id)
        organization = SwitchKeysRequest.call(
            url=url,
            method=SwitchKeysRequestMethod.PUT,
            data=data,
            token=self.api_token,
        )

        if organization.error_message:
            raise ResponseError(organization.error_message)

        return parse_organization(organization.data)

    def get(
        self, organization_id: int
    ) -> SwitchKeysOrganizationResponse | ResponseError:
        """
        Method to get an organization.

        Args:
          organization_id (int): the organization ID.

        Raises:
          ResponseError: If there is an error while requesting.
        """

        url = self.__routes.get_route(EndPoints.ORGANIZATIONS_ID, organization_id)
        organization = SwitchKeysRequest.call(
            url=url,
            method=SwitchKeysRequestMethod.GET,
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
        organization = SwitchKeysRequest.call(
            url=url, method=SwitchKeysRequestMethod.DELETE, token=self.api_token
        )

        if (
            organization.error_message
            and organization.error_message.lower() == "empty response content"
        ):
            return "Deleted"

        if organization.error_message:
            raise ResponseError(organization.error_message)

        return "Deleted"
