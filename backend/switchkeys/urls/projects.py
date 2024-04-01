from django.urls import path


from switchkeys.views.projects import (
    BaseOrganizationProjectApiView,
    OrganizationProjectApiView,
)

urlpatterns = [
    path("", BaseOrganizationProjectApiView.as_view()),
    path("<str:project_id>/", OrganizationProjectApiView.as_view()),
]
