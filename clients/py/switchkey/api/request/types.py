from enum import Enum
from typing import List

from switchkeys.api.response.types import SwitchKeysUserResponse


class SwitchKeysOrganizationRequestType:
    # TODO: Will be used in next version as an interface for the request payload.
    """
    Represents a Type object for organizations.

    Attributes:
        name (str): The name of the organization.
        members (List[SwitchKeysUserType]): The members of the organization.

    Methods:
        N/A
    """

    def __init__(
        self,
        name: str,
        members: List[SwitchKeysUserResponse],
    ):
        """
        Initialize the SwitchKeysOrganizationRequestType object.

        Args:
            name (str): The name of the organization.
            members (List[SwitchKeysUserType]): The members of the organization.
        """
        self.name = name
        self.members = members


class SwitchKeysProjectRequestType:
    # TODO: Will be used in next version as an interface for the request payload.
    """
    Represents a Type object for projects.

    Attributes:
        name (str): The name of the project.
        members (List[SwitchKeysUserType]): The members of the organization.

    Methods:
        N/A
    """

    def __init__(
        self,
        name: str,
        organization_id: int,
    ):
        """
        Initialize the SwitchKeysOrganizationRequestType object.

        Args:
            name (str): The name of the organization.
            organization_id (int): The ID of the organization.
        """
        self.name = name
        self.organization_id = organization_id

class UserTypeEnum(Enum):
    ADMINISTRATOR = "Administrator"
    USER = "User"