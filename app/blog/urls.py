from django.urls import path

from .views import (
    PostCreateView,
    PostListView,
    ReadStatusCreateView,
    SubscriptionCreateView,
    SubscriptionDeleteView,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post-list"),
    path("new/post/", PostCreateView.as_view(), name="post-create"),
    path("subscribe/", SubscriptionCreateView.as_view(), name="subscription-create"),
    path("unsubscribe/<int:pk>/", SubscriptionDeleteView.as_view(), name="unsubscribe-delete"),
    path("is/read/", ReadStatusCreateView.as_view(), name="read-status-create"),
]
