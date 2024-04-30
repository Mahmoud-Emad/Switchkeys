from django.urls import path

from switchkeys.views.environments import (
    BaseProjectEnvironmentApiView,
    ProjectEnvironmentApiView,
    # GetUserFeatureValueAPIView,
    # OrganizationProjectEnvironmentKeyApiView,
    # AddUserEnvironmentFeatureApiView,
    # AddUserEnvironmentFeaturesApiView,
    # BaseEnvironmentFeatureAPIView,
    # AddEnvironmentUserAPIView,
    # AddEnvironmentUsersAPIView,
    # RemoveEnvironmentUserAPIView,
)

urlpatterns = [
    path("", BaseProjectEnvironmentApiView.as_view()),
    path("<str:environment_id>/", ProjectEnvironmentApiView.as_view()),
    # path(
    #     "key/<str:environment_key>/", OrganizationProjectEnvironmentKeyApiView.as_view()
    # ),
    # path("key/<str:environment_key>/add-user/", AddEnvironmentUserAPIView.as_view()),
    # path("key/<str:environment_key>/add-users/", AddEnvironmentUsersAPIView.as_view()),
    # path(
    #     "key/<str:environment_key>/remove-user/", RemoveEnvironmentUserAPIView.as_view()
    # ),
    # path(
    #     "key/<str:environment_key>/features/", BaseEnvironmentFeatureAPIView.as_view()
    # ),
    # path(
    #     "key/<str:environment_key>/user/add-feature/",
    #     AddUserEnvironmentFeatureApiView.as_view(),
    # ),
    # path(
    #     "key/<str:environment_key>/user/add-features/",
    #     AddUserEnvironmentFeaturesApiView.as_view(),
    # ),
    # path(
    #     "key/<str:environment_key>/user/get-feature/",
    #     GetUserFeatureValueAPIView.as_view(),
    # ),
]
