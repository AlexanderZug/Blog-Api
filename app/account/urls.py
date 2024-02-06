from django.urls import path

from .views import (
    SignInCreateView,
    SignOutView,
    SignView,
    UserPostListView,
    UserRetrieveUpdateDestroyView,
    UserSubscriptionView,
    VerifyTokenCreateView,
)

urlpatterns = [
    path("", UserRetrieveUpdateDestroyView.as_view()),
    path("token/", VerifyTokenCreateView.as_view()),
    path("sign/", SignView.as_view()),
    path("sign/in/", SignInCreateView.as_view()),
    path("sign/out/", SignOutView.as_view()),
    path("posts/me/", UserPostListView.as_view()),
    path("subscriptions/me/", UserSubscriptionView.as_view()),
]
