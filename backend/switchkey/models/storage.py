""" The storage file will include all related modales e.g. the key_value storage """

from switchkey.models.abstracts import TimeStamp
from switchkey.models.users import User
from django.db import models


class KeyValueStorage(TimeStamp):
  user = models.ForeignKey(User, related_name="user_keys", on_delete=models.CASCADE)
  key = models.CharField(max_length=20)
  value = models.TextField(max_length=1000)
  last_used = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Key Value Storage'
    verbose_name_plural = 'Key Value Storage'
    unique_together = (
      "user",
      "key",
    )

  def __str__(self) -> str:
    return f'{self.user.full_name} | {self.key}'
