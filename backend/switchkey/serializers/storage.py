from rest_framework.serializers import ModelSerializer

from switchkey.models.storage import KeyValueStorage

class KeyValueStorageSerializer(ModelSerializer):
  class Meta:
    model = KeyValueStorage
    fields = ["user", "key", "value",]
