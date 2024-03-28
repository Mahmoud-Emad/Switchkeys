from django.urls import path

from switchkey.views.organizations import BaseOrganizationApiView, OrganizationApiView

urlpatterns = [
    path("", BaseOrganizationApiView.as_view()),
    path("<str:organization_id>/", OrganizationApiView.as_view()),
]
