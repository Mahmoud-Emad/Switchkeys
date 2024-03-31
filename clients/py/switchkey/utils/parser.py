from typing import Any, Dict, List

from switchkey.api.interfaces.response import (
    SwitchKeyOrganizationResponse,
    SwitchKeyProjectResponse,
    SwitchKeyUserResponse,
)


def parse_user(
    user_data: Dict[str, Any]
) -> SwitchKeyUserResponse | List[SwitchKeyUserResponse]:
    """
    Parse user data.

    Args:
        user_data (Dict[str, Any]): User data to be parsed.

    Returns:
        SwitchKeyUserType | List[SwitchKeyUserType]: Parsed user object or list of parsed user objects.
    """

    if type(user_data) == list:
        users: List[SwitchKeyUserResponse] = []
        for user in user_data:
            users.append(
                SwitchKeyUserResponse(
                    background_color=user.get("background_color"),
                    email=user.get("email"),
                    first_name=user.get("first_name"),
                    full_name=user.get("full_name"),
                    is_active=user.get("is_active"),
                    id=user.get("id"),
                    joining_at=user.get("joining_at"),
                    last_name=user.get("last_name"),
                )
            )
    else:
        return SwitchKeyUserResponse(
            background_color=user_data.get("background_color"),
            email=user_data.get("email"),
            first_name=user_data.get("first_name"),
            full_name=user_data.get("full_name"),
            is_active=user_data.get("is_active"),
            id=user_data.get("id"),
            joining_at=user_data.get("joining_at"),
            last_name=user_data.get("last_name"),
        )


def parse_organization(
    organization_data: Dict[str, Any]
) -> SwitchKeyOrganizationResponse:
    """
    Parse organization data.

    Args:
        organization_data (Dict[str, Any]): Organization data to be parsed.

    Returns:
        SwitchKeyOrganizationResponse: Parsed organization object.
    """

    return SwitchKeyOrganizationResponse(
        id=organization_data.get("id"),
        name=organization_data.get("name"),
        created=organization_data.get("created"),
        modified=organization_data.get("modified"),
        members=parse_user(organization_data.get("members")),
        owner=parse_user(organization_data.get("owner")),
    )


def parse_project(project_data: Dict[str, Any]) -> SwitchKeyProjectResponse:
    """
    Parse project data.

    Args:
        project_data (Dict[str, Any]): Project data to be parsed.

    Returns:
        SwitchKeyProjectResponse: Parsed project object.
    """

    return SwitchKeyProjectResponse(
        id=project_data.get("id"),
        name=project_data.get("name"),
        created=project_data.get("created"),
        modified=project_data.get("modified"),
        organization=parse_organization(project_data.get("organization")),
    )
