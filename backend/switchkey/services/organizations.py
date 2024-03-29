from typing import List
from switchkey.models.management import Organization


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
