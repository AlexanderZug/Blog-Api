from __future__ import annotations

import contextlib
import datetime
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Manager
from django.utils import timezone

with contextlib.suppress(ImportError):
    from blog.models import Blog, ReadStatus, Subscription


class User(AbstractUser):
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    username = models.CharField(
        "Логин",
        max_length=150,
        default=uuid.uuid4,
        unique=True,
    )
    email = models.EmailField("Email", unique=True)
    blog: Blog | Manager
    subscriptions: Subscription | Manager
    verify_tokens: VerifyToken | Manager
    read_statuses: ReadStatus | Manager

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return str(self.first_name)


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
    )
    last_name = models.CharField(
        "фамилия",
        max_length=80,
        blank=True,
    )
    email = models.EmailField("Email", blank=True, null=True, unique=True)
    token = models.PositiveIntegerField("Токен")
    uuid = models.UUIDField("Uuid", default=uuid.uuid4)
    activation_date = models.DateTimeField("Дата деактивации", auto_now_add=True)

    class Meta:
        verbose_name = "Токен"
        verbose_name_plural = "Токены"

    def __str__(self) -> str:
        return str(self.email)

    @property
    def email_expired(self) -> bool:
        return self.activation_date + datetime.timedelta(hours=1) < timezone.now()
