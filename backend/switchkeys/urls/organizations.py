from django.urls import path

from switchkeys.views.organizations import (
    BaseOrganizationApiView,
    OrganizationApiView,
    OrganizationByNameApiView,
    OrganizationAddMemberApiView,
    OrganizationRemoveMemberApiView,
    OrganizationProjectsApiView,
)

urlpatterns = [
    path("", BaseOrganizationApiView.as_view()),
    path("<str:organization_id>/projects/", OrganizationProjectsApiView.as_view()),
    path("<str:organization_id>/", OrganizationApiView.as_view()),
    path("name/<str:organization_name>/", OrganizationByNameApiView.as_view()),
    path("<str:organization_id>/add-member/", OrganizationAddMemberApiView.as_view()),
    path(
        "<str:organization_id>/remove-member/",
        OrganizationRemoveMemberApiView.as_view(),
    ),
]
