from django.urls import path

from switchkeys.views.groups import (
    BaseOrganizationProjectGroupApiView,
    OrganizationProjectGroupApiView,
)

urlpatterns = [
    path("", BaseOrganizationProjectGroupApiView.as_view()),
    path("<str:group_id>/", OrganizationProjectGroupApiView.as_view()),
]
