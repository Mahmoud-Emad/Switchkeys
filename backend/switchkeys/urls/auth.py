from django.urls import path

from switchkeys.views.auth import (
    RegisterApiView,
    LoginByTokenApiView,
    MyTokenRefreshView,
    ChangePasswordView,
)


urlpatterns = [
    path("signup/", RegisterApiView.as_view()),
    path("login/", LoginByTokenApiView.as_view()),
    path("token/refresh/", MyTokenRefreshView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
]
