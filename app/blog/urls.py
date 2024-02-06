from django.urls import path

from .views import SubscriptionCreateView, SubscriptionDeleteView

urlpatterns = [
    path("subscribe/", SubscriptionCreateView.as_view()),
    path("unsubscribe/<int:pk>/", SubscriptionDeleteView.as_view()),
]
