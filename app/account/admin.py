from django.contrib import admin
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
    list_display = ("first_name", "last_name", "email", "get_users_posts")
    list_display_links = ("first_name", "last_name", "email")

    @admin.display(description="Количество постов")
    def get_users_posts(self, obj):
        return obj.blog.posts.count()


admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(PeriodicTask)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
