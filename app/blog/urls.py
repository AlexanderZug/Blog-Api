from django.urls import path

from .views import (
    PostCreateView,
    PostListView,
    ReadStatusCreateView,
    SubscriptionCreateView,
    SubscriptionDeleteView,
)

urlpatterns = [
    path("posts/", PostListView.as_view()),
    path("new/post/", PostCreateView.as_view()),
    path("subscribe/", SubscriptionCreateView.as_view(), name="subscription-create"),
    path("unsubscribe/<int:pk>/", SubscriptionDeleteView.as_view()),
    path("is/read/", ReadStatusCreateView.as_view()),
]
