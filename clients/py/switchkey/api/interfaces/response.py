from typing import List


class SwitchKeyUserResponse:
    """
    Represents a Type object for users.

    Attributes:
        id (int): The unique identifier of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        full_name (str): The full name of the user.
        email (str): The email address of the user.
        joining_at (str): The date/time when the user joined.
        background_color (str): The background color associated with the user.
        is_active (bool): Indicates whether the user is active.

    Methods:
        N/A
    """

    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        full_name: str,
        email: str,
        joining_at: str,
        background_color: str,
        is_active: bool,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.joining_at = joining_at
        self.background_color = background_color
        self.is_active = is_active

class SwitchKeyOrganizationResponse:
    """
    Represents a Type object for organizations.

    Attributes:
        id (int): [READONLY FIELD] -> The unique identifier of the organization.
        name (str): The name of the organization.
        owner (SwitchKeyUser): The owner of the organization.
        members (List[SwitchKeyUser]): The members of the organization.
        created (str): [READONLY FIELD] -> The date/time when the organization was created.
        modified (str): [READONLY FIELD] -> The date/time when the organization was last modified.

    Methods:
        N/A
    """

    def __init__(
        self,
        id: int,
        name: str,
        owner: SwitchKeyUserResponse,
        members: List[SwitchKeyUserResponse],
        created: str,
        modified: str,
    ):
        """
        Initialize the SwitchKeyOrganizationResponse object.

        Args:
            id (int): The unique identifier of the organization.
            name (str): The name of the organization.
            owner (SwitchKeyUserResponse): The owner of the organization.
            members (List[SwitchKeyUserResponse]): The members of the organization.
            created (str): The date/time when the organization was created.
            modified (str): The date/time when the organization was last modified.
        """
        self.id = id
        self.name = name
        self.owner = owner
        self.members = members
        self.created = created
        self.modified = modified


class SwitchKeyProjectResponse:
    """
    Represents a Type object for project response.

    Attributes:
        id (int): The unique identifier of the project.
        name (str): The name of the project.
        organization (SwitchKeyOrganizationResponse): The organization to which the project belongs.
        created (str): The date/time when the project was created.
        modified (str): The date/time when the project was last modified.

    Methods:
        N/A
    """
    # from switchkey.api.organization import SwitchKeyOrganization, SwitchKeyOrganizationResponse

    def __init__(
        self,
        id: int,
        name: str,
        organization: SwitchKeyOrganizationResponse,
        created: str,
        modified: str,
    ):
        self.id = id
        self.name = name
        self.organization = organization
        self.created = created
        self.modified = modified