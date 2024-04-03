from typing import List
from switchkeys.models.management import OrganizationProject, Organization


def get_all_projects() -> List[OrganizationProject]:
    """Return all projects"""
    return OrganizationProject.objects.all().order_by("name")


def get_all_organization_projects(
    organization: Organization,
) -> List[OrganizationProject]:
    """Return all organization projects"""
    return OrganizationProject.objects.filter(organization=organization).order_by(
        "name"
    )


def check_project_name(project_name: str, organization_id: int):
    """
    Check if there is projects created on an exact organization by the requested user with the same name
    """
    projects = OrganizationProject.objects.filter(
        name=project_name, organization__id=organization_id
    )
    return len(projects) > 0


def get_project_by_id(id: str) -> OrganizationProject:
    """Return project who has the same id"""
    if not id.isdigit():
        return None
    try:
        return OrganizationProject.objects.get(id=int(id))
    except OrganizationProject.DoesNotExist:
        return None
