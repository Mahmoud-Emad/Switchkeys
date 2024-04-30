from enum import Enum
from typing import List
from switchkeys.models.users import DeviceType, ProjectEnvironmentUser, User, UserDevice
from switchkeys.models.environments import EnvironmentFeature
from switchkeys.models.management import (
    Organization,
    ProjectEnvironment,
    OrganizationProject,
)


class EnvironmentsName(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


def get_all_environments() -> List[ProjectEnvironment]:
    """Return all environments"""
    return ProjectEnvironment.objects.all().order_by("name")


def get_all_project_environments(
    project_id: OrganizationProject,
) -> List[OrganizationProject]:
    """Return all project environments"""
    return ProjectEnvironment.objects.filter(project__id=project_id).order_by("name")


def get_environment_by_id(id: str) -> ProjectEnvironment:
    """Return project environment who has the same id"""
    if not id.isdigit():
        return None
    try:
        return ProjectEnvironment.objects.get(id=int(id))
    except ProjectEnvironment.DoesNotExist:
        return None


def get_environment_by_key(environment_key: str) -> ProjectEnvironment | None:
    """Return project environment who has the same id"""
    try:
        return ProjectEnvironment.objects.get(environment_key=str(environment_key))
    except ProjectEnvironment.DoesNotExist:
        return None


def get_environment_user_by_id(user_id: str) -> ProjectEnvironmentUser | None:
    """Return project environment who has the same id"""
    if not user_id.isdigit():
        return None
    try:
        return ProjectEnvironmentUser.objects.get(id=int(user_id))
    except ProjectEnvironmentUser.DoesNotExist:
        return None


def get_environment_user_username(username: str) -> ProjectEnvironmentUser | None:
    """Check and return the user if created or none if not."""
    try:
        return ProjectEnvironmentUser.objects.get(username=username)
    except ProjectEnvironmentUser.DoesNotExist:
        return None


def create_environment_user(
    username: str, device_type: DeviceType, device_version: str
) -> ProjectEnvironmentUser | None:
    """Create the user."""
    device = UserDevice.objects.get_or_create(
        device_type=device_type, version=device_version
    )

    return ProjectEnvironmentUser.objects.create(username=username, device=device[0])


def get_all_environment_features(
    environment: ProjectEnvironment,
) -> List[EnvironmentFeature]:
    return EnvironmentFeature.objects.filter(environment__id=environment.id)


def create_environments(project: OrganizationProject) -> List[ProjectEnvironment]:
    """When creating new projects, we need to create three environments: Development, Staging, and Production."""
    ProjectEnvironment.objects.get_or_create(
        project=project, name=EnvironmentsName.DEVELOPMENT.value
    )

    ProjectEnvironment.objects.get_or_create(
        project=project, name=EnvironmentsName.STAGING.value
    )

    ProjectEnvironment.objects.get_or_create(
        project=project, name=EnvironmentsName.PRODUCTION.value
    )

    return ProjectEnvironment.objects.filter(project=project)


def validate_unique_environment_name(
    environment_name: str, project: OrganizationProject
) -> bool:
    """
    Check if the user has an environment with the same name.

    ### Attributes
        - environment_name (str): The environment name.
        - project (OrganizationProject): The project to get all it's environments.

    ### Returns
        - True, if the name is exist on the user.
        - False, if the name is not created before by the use.
    """

    environments = ProjectEnvironment.objects.filter(
        project=project, name=environment_name
    )

    return environments.__len__() > 0
