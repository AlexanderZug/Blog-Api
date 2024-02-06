from django.contrib import admin

from .models import Blog, Post, Subscription


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "created_at", "blog")
    list_display_links = ("title", "text")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_display_links = ("user",)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("subscriber", "blog")
    list_display_links = ("subscriber", "blog")
