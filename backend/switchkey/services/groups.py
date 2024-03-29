from typing import List
from switchkey.models.management import OrganizationProjectGroup, OrganizationProject


def get_all_groups() -> List[OrganizationProjectGroup]:
    """Return all groups"""
    return OrganizationProjectGroup.objects.all().order_by("name")


def get_all_project_groups(
    project_id: OrganizationProject,
) -> List[OrganizationProject]:
    """Return all project groups"""
    return OrganizationProjectGroup.objects.filter(project__id=project_id).order_by(
        "name"
    )


def get_group_by_id(id: str) -> OrganizationProjectGroup:
    """Return project group who has the same id"""
    if not id.isdigit():
        return None
    try:
        return OrganizationProjectGroup.objects.get(id=int(id))
    except OrganizationProjectGroup.DoesNotExist:
        return None
