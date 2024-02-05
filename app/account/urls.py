from django.urls import path

from .views import (
    SignInCreateView,
    SignOutView,
    SignView,
    UserRetrieveUpdateDestroyView,
    VerifyTokenCreateView,
)

urlpatterns = [
    path("", UserRetrieveUpdateDestroyView.as_view()),
    path("token/", VerifyTokenCreateView.as_view()),
    path("sign/", SignView.as_view()),
    path("sign/in/", SignInCreateView.as_view()),
    path("sign/out/", SignOutView.as_view()),
]
