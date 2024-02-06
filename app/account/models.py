from __future__ import annotations

import datetime
import uuid
from typing import Union

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Manager
from django.utils import timezone

try:
    from blog.models import Blog, ReadStatus, Subscription
except ImportError:
    pass


class User(AbstractUser):
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    username = models.CharField(
        "Логин", max_length=150, default=uuid.uuid4, unique=True
    )
    email = models.EmailField("Email", unique=True)
    blog: Union[Blog, Manager]
    subscriptions: Union[Subscription, Manager]
    verify_tokens: Union[VerifyToken, Manager]
    read_statuses: Union[ReadStatus, Manager]

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class VerifyToken(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="verify_tokens",
        verbose_name="Пользователь",
    )
    first_name = models.CharField(
        "имя",
        max_length=70,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        "фамилия",
        max_length=80,
        blank=True,
        null=True,
    )
    email = models.EmailField("Email", blank=True, null=True, unique=True)
    token = models.PositiveIntegerField("Токен")
    uuid = models.UUIDField("Uuid", default=uuid.uuid4)
    activation_date = models.DateTimeField("Дата деактивации", auto_now_add=True)

    @property
    def email_expired(self) -> bool:
        return self.activation_date + datetime.timedelta(hours=1) < timezone.now()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Токен"
        verbose_name_plural = "Токены"
