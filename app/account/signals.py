from blog.models import Blog
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User)
def attach_blog_to_new_user(instance: User, created, *args, **kwargs):
    if created:
        Blog.objects.create(user=instance)
