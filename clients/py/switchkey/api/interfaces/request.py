from typing import List

from switchkey.api.interfaces.response import SwitchKeyUserResponse


class SwitchKeyOrganizationRequestType:
    # TODO: Will be used in next version as an interface for the request payload.
    """
    Represents a Type object for organizations.

    Attributes:
        name (str): The name of the organization.
        members (List[SwitchKeyUserType]): The members of the organization.

    Methods:
        N/A
    """

    def __init__(
        self,
        name: str,
        members: List[SwitchKeyUserResponse],
    ):
        """
        Initialize the SwitchKeyOrganizationRequestType object.

        Args:
            name (str): The name of the organization.
            members (List[SwitchKeyUserType]): The members of the organization.
        """
        self.name = name
        self.members = members


class SwitchKeyProjectRequestType:
    # TODO: Will be used in next version as an interface for the request payload.
    """
    Represents a Type object for projects.

    Attributes:
        name (str): The name of the project.
        members (List[SwitchKeyUserType]): The members of the organization.

    Methods:
        N/A
    """

    def __init__(
        self,
        name: str,
        organization_id: int,
    ):
        """
        Initialize the SwitchKeyOrganizationRequestType object.

        Args:
            name (str): The name of the organization.
            organization_id (int): The ID of the organization.
        """
        self.name = name
        self.organization_id = organization_id
