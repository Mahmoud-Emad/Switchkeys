from django.urls import path


from switchkeys.views.users import (
    GeneralUserAPIView,
    BaseGeneralUserAPIView,
)


urlpatterns = [
    path("", BaseGeneralUserAPIView.as_view()),
    path("<str:id>/", GeneralUserAPIView.as_view()),
]
