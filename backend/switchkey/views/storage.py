from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from switchkey.services.storage import get_all_keys, get_key_by_id
from switchkey.api.custom_response import CustomResponse
from switchkey.serializers.storage import KeyValueStorageSerializer


class BaseKeyValueStorageApiView(ListAPIView):
  serializer_class = KeyValueStorageSerializer

  def get_queryset(self) -> Response:
    """Get all keys in the system"""
    query_set = get_all_keys()
    return query_set

  def post(self, request: Request) -> Response:
    """Get key by id"""

    key = request.data
    serializer = self.get_serializer(key)
    if serializer.is_valid():
      serializer.save()
      return CustomResponse.success(
        data=KeyValueStorageSerializer(key).data,
        message="Key found."
      )
    return CustomResponse.bad_request(
      message="Please make sure that you entered a valid data.",
      error=serializer.errors,
      data=request.data,
    )



class KeyValueStorageApiView(GenericAPIView):
  serializer_class = KeyValueStorageSerializer

  def get(self, request: Request, key_id: str) -> Response:
    """Get key by id"""
    key = get_key_by_id(key_id)
    if key is None:
      return CustomResponse.not_found(message="The key is not exist.")
    return CustomResponse.success(
      data=KeyValueStorageSerializer(key).data,
      message="Key found."
    )
