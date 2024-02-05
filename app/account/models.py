from __future__ import annotations

import uuid
from typing import Union

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Manager


try:
    from blog.models import Blog, Subscription
except ImportError:
    pass


class User(AbstractUser):
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    username = models.CharField(
        "Логин", max_length=150, default=uuid.uuid4, unique=True
    )
    blog: Union[Blog, Manager]
    subscriptions: Union[Subscription, Manager]

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
