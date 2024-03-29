from django.urls import path


from switchkey.views.projects import (
    BaseOrganizationProjectApiView,
    OrganizationProjectApiView,
)

urlpatterns = [
    path("", BaseOrganizationProjectApiView.as_view()),
    path("<str:project_id>/", OrganizationProjectApiView.as_view()),
]
