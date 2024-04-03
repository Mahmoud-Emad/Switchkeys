from django.urls import path

from switchkeys.views.organizations import (
    BaseOrganizationApiView,
    OrganizationApiView,
    OrganizationByNameApiView,
)

urlpatterns = [
    path("", BaseOrganizationApiView.as_view()),
    path("<str:organization_id>/", OrganizationApiView.as_view()),
    path("name/<str:organization_name>/", OrganizationByNameApiView.as_view()),
]
