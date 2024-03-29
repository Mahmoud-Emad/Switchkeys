from django.urls import path

from switchkey.views.groups import BaseOrganizationProjectGroupApiView, OrganizationProjectGroupApiView

urlpatterns = [
    path("", BaseOrganizationProjectGroupApiView.as_view()),
    path("<str:group_id>/", OrganizationProjectGroupApiView.as_view()),
]
