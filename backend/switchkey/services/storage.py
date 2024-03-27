from typing import List

from switchkey.models.storage import KeyValueStorage
from switchkey.models.users import User

def get_all_keys() -> List[KeyValueStorage]:
  """Get all keys in the system"""
  return KeyValueStorage.objects.all()

def get_key_by_id(key_id: str) -> List[KeyValueStorage] | None:
  """Get key by its ID"""
  if key_id.isdigit():
    try:
      return KeyValueStorage.objects.get(id=int(key_id))
    except KeyValueStorage.DoesNotExist:
      return None
  return None

def get_user_keys(user: User) -> List[KeyValueStorage]:
  """Filter keys based on the requested user"""
  return KeyValueStorage.objects.filter(user=user)

