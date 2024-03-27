"""This file will containes everything related to User model."""

from typing import List
from switchkey.models.users import User

def get_user_by_id(id: str) -> User:
    """Return user who have the same id"""
    if id is None:
        return id
    try:
        return User.objects.get(id=int(id))
    except User.DoesNotExist:
        return None

def get_all_users() -> List[User]:
    """Return all registered users"""
    return User.objects.all()

def get_user_by_email(email: str) -> User:
    """Return user who have the same email"""
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None
