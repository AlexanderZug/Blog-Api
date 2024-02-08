from django.contrib import admin
from django.contrib.auth.models import Group
from django_celery_beat.models import (
    ClockedSchedule,
    CrontabSchedule,
    IntervalSchedule,
    PeriodicTask,
    SolarSchedule,
)

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "get_users_posts"]
    list_display_links = ["first_name", "last_name", "email"]

    @admin.display(description="Количество постов у пользователя")
    def get_users_posts(self, obj) -> int:
        return obj.blog.posts.count()

    def has_add_permission(self, request) -> bool:
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None) -> bool:
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None) -> bool:
        return request.user.is_superuser


admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(PeriodicTask)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(Group)
