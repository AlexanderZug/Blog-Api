from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "get_users_posts")
    list_display_links = ("first_name", "last_name", "email")

    @admin.display(description="Количество постов")
    def get_users_posts(self, obj):
        return obj.blog.posts.count()
