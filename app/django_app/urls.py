from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django_app.settings import PROJECT_NAME

urlpatterns = [
    path("api/grappelli/", include("grappelli.urls")),
    path("api/admin/", admin.site.urls),
    path("api/", include("api.urls")),
]

urlpatterns += (
    re_path(r"^api/media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
)
urlpatterns += (
    re_path(
        r"^api/static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}
    ),
)

admin.site.site_header = f"{PROJECT_NAME} Administration"
admin.site.site_title = PROJECT_NAME
admin.site.index_title = f"{PROJECT_NAME} Administration"
