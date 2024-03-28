from django.urls import path


from switchkey.views.management import (
    BaseKeyValueStorageApiView,
    KeyValueStorageApiView,
)

urlpatterns = [
    path("", BaseKeyValueStorageApiView.as_view()),
    path("<str:key_id>/", KeyValueStorageApiView.as_view()),
]
