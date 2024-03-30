from typing import List
from switchkey.models.users import ProjectEnvironmentUser
from switchkey.models.management import ProjectEnvironment, OrganizationProject


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


def get_environment_by_key(environment_key: str) -> ProjectEnvironment:
    """Return project environment who has the same id"""
    try:
        return ProjectEnvironment.objects.get(environment_key=str(environment_key))
    except ProjectEnvironment.DoesNotExist:
        return None

def get_environment_user(user_id: str):
    """Return project environment who has the same id"""
    if not user_id.isdigit():
        return None
    try:
        return ProjectEnvironmentUser.objects.get(id = int(user_id))
    except ProjectEnvironmentUser.DoesNotExist:
        return None
