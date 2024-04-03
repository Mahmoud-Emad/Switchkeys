from django.urls import path

from switchkeys.views.environments import (
    BaseOrganizationProjectEnvironmentApiView,
    OrganizationProjectEnvironmentApiView,
    OrganizationProjectEnvironmentKeyApiView,
    SetEnvironmentKeyApiView,
    BaseEnvironmentFeatureAPIView,
    AddEnvironmentUserAPIView,
)

urlpatterns = [
    path("", BaseOrganizationProjectEnvironmentApiView.as_view()),
    path("<str:environment_id>/", OrganizationProjectEnvironmentApiView.as_view()),
    path(
        "key/<str:environment_key>/", OrganizationProjectEnvironmentKeyApiView.as_view()
    ),
    path("key/<str:environment_key>/add-user/", AddEnvironmentUserAPIView.as_view()),
    path("key/<str:environment_key>/user/set/", SetEnvironmentKeyApiView.as_view()),
    path(
        "key/<str:environment_key>/features/", BaseEnvironmentFeatureAPIView.as_view()
    ),
]
