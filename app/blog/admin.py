from django.contrib import admin

from .models import Blog, Post, Subscription


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "created_at", "blog"]
    list_display_links = ["title", "text"]
    search_fields = ["title", "text"]

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None) -> bool:
        return False


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["user"]
    list_display_links = ["user"]

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["subscriber", "blog"]
    list_display_links = ["subscriber", "blog"]

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None) -> bool:
        return False
