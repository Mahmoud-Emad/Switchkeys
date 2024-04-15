from django.urls import path


from switchkeys.views.users import (
    GeneralUserAPIView,
    BaseGeneralUserAPIView,
    GetUserByEmailAPIView,
)


urlpatterns = [
    path("", BaseGeneralUserAPIView.as_view()),
    path("email/<str:email>/", GetUserByEmailAPIView.as_view()),
    path("<str:id>/", GeneralUserAPIView.as_view()),
]
