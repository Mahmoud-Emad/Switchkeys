from django.urls import path

from switchkeys.views.environments import (
    AddEnvironmentUserAPIView,
    RemoveEnvironmentUserAPIView,
    BaseProjectEnvironmentApiView,
    DeleteEnvironmentFeatureAPIView,
    ProjectEnvironmentApiView,
    ProjectEnvironmentKeyApiView,
    BaseEnvironmentFeatureAPIView,
    UpdateEnvironmentFeatureAPIView,
    EnvironmentUserFeaturesApiView,
    SetEnvironmentUserFeaturesApiView,
    DeleteEnvironmentUserFeature,
)

urlpatterns = [
    path("", BaseProjectEnvironmentApiView.as_view()),
    path("<str:environment_id>/", ProjectEnvironmentApiView.as_view()),
    path("key/<str:environment_key>/", ProjectEnvironmentKeyApiView.as_view()),
    path("key/<str:environment_key>/add-user/", AddEnvironmentUserAPIView.as_view()),
    path(
        "key/<str:environment_key>/remove-user/", RemoveEnvironmentUserAPIView.as_view()
    ),
    path(
        "key/<str:environment_key>/features/", BaseEnvironmentFeatureAPIView.as_view()
    ),
    path(
        "key/<str:environment_key>/features/delete/<str:feature_name>/",
        DeleteEnvironmentFeatureAPIView.as_view(),
    ),
    path(
        "key/<str:environment_key>/features/update/<str:feature_name>/",
        UpdateEnvironmentFeatureAPIView.as_view(),
    ),
    path(
        "key/<str:environment_key>/users/<str:username>/features/",
        EnvironmentUserFeaturesApiView.as_view(),
    ),
    path(
        "key/<str:environment_key>/users/<str:username>/features/set/",
        SetEnvironmentUserFeaturesApiView.as_view(),
    ),
    path(
        "key/<str:environment_key>/users/<str:username>/features/delete/<feature_name>/",
        DeleteEnvironmentUserFeature.as_view(),
    ),
    # path(
    #     "key/<str:environment_key>/users/<str:username>/features/add/",
    #     AddEnvironmentUserFeatureApiView.as_view(),
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
