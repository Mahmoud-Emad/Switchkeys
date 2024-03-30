from django.urls import path

from switchkey.views.environments import (
    BaseOrganizationProjectEnvironmentApiView,
    OrganizationProjectEnvironmentApiView,
    OrganizationProjectEnvironmentKeyApiView,
)

urlpatterns = [
    path("", BaseOrganizationProjectEnvironmentApiView.as_view()),
    path("<str:environments_id>/", OrganizationProjectEnvironmentApiView.as_view()),
    path(
        "key/<str:environment_key>/", OrganizationProjectEnvironmentKeyApiView.as_view()
    ),
]
