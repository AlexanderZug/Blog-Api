from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .base import urlpatterns as base_url_patterns

urlpatterns = [
    path("", RedirectView.as_view(url="swagger/")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("post/", include("blog.urls")),
    path("account/", include("account.urls")),
]

urlpatterns += base_url_patterns
