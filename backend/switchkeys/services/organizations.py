from typing import List
from switchkeys.models.users import User
from switchkeys.models.management import Organization


def get_all_organization() -> List[Organization]:
    """Return all organization"""
    return Organization.objects.all().order_by("name")


def get_organization_by_id(id: str) -> Organization:
    """Return organization who has the same id"""
    if not id.isdigit():
        return None
    try:
        return Organization.objects.get(id=int(id))
    except Organization.DoesNotExist:
        return None

def check_organization_name(user: User, name: str):
    """Check if there is an organization created by the requested user with the same name"""
    organizations = Organization.objects.filter(
        name = name,
        owner__id = user.id
    )
    return len(organizations) > 0