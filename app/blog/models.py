from __future__ import annotations

from typing import Union

from account.models import User
from django.db import models
from django.db.models import Manager


class Blog(models.Model):
    title = models.CharField("Заголовок", max_length=100, blank=True, null=True)
    user = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        related_name="blog",
        on_delete=models.CASCADE,
        help_text="Пользователь может иметь только один блог",
    )
    posts: Union[Post, Manager]
    subscribers: Union[Subscription, Manager]

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    text = models.CharField("Текст", max_length=140)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    blog = models.ForeignKey(
        Blog,
        verbose_name="Блог",
        related_name="posts",
        on_delete=models.CASCADE,
    )
    read_statuses: Union[ReadStatus, Manager]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        User,
        verbose_name="Подписчик",
        related_name="subscriptions",
        on_delete=models.CASCADE,
    )
    blog = models.ForeignKey(
        Blog,
        verbose_name="Блог",
        related_name="subscribers",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class ReadStatus(models.Model):
    user = models.ForeignKey(
        User, related_name="read_statuses", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name="read_statuses", on_delete=models.CASCADE
    )
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Статус прочтения"
        verbose_name_plural = "Статусы прочтения"
