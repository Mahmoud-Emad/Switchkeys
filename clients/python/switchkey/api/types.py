from typing import List, Dict, Any


class DeviceResponse:
    # Its not serialized yet.
    def __init__(self):
        pass


class ProjectUserResponse:

    def __init__(
        self, id: int, username: str, device: DeviceResponse, features: Dict[str, Any]
    ):
        self.id = id
        self.username = username
        self.device = device
        self.features = features


class UserResponse:

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


class OrganizationResponse:

    def __init__(
        self,
        id: int,
        name: str,
        owner: UserResponse,
        members: List[UserResponse],
        created: str,
        modified: str,
    ):
        self.id = id
        self.name = name
        self.owner = owner
        self.members = members
        self.created = created
        self.modified = modified


class ProjectResponse:

    def __init__(
        self,
        id: int,
        name: str,
        created: str,
        modified: str,
        organization: OrganizationResponse,
    ):
        self.id = id
        self.name = name
        self.organization = organization
        self.created = created
        self.modified = modified


class EnvironmentResponse:

    def __init__(
        self,
        id: int,
        name: str,
        created: str,
        modified: str,
        project: ProjectResponse,
        environment_key: str,
        users: List[ProjectUserResponse],
    ):
        self.id = id
        self.name = name
        self.project = project
        self.created = created
        self.modified = modified
        self.environment_key = environment_key
        self.users = users
