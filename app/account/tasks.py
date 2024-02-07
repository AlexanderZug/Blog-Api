from blog.models import Post, Subscription
from celery import shared_task
from django.db.models import Q
from django.utils import timezone
from utils.mail_service import send_email

from .models import VerifyToken


@shared_task
def verify_token_cleanup_scheduler() -> None:
    verify_token = VerifyToken.objects.filter(
        Q(activation_date__lt=timezone.now() - timezone.timedelta(hours=1))
    )
    for token in verify_token:
        if token.email_expired:
            token.delete()


@shared_task
def send_email_notification() -> None:
    yesterday = timezone.now() - timezone.timedelta(days=1)
    subscriptions = Subscription.objects.select_related("subscriber", "blog").filter(
        subscriber__is_active=True
    )

    for subscription in subscriptions:
        recent_posts = Post.objects.filter(
            blog=subscription.blog, created_at__gte=yesterday
        ).order_by("-created_at")[:5]

        recipient_email = subscription.subscriber.email

        subject = "Актуальные посты"
        message = f"Ваши актуальные посты из блога {subscription.blog.title}:\n\n"
        for post in recent_posts:
            message += f"- {post.title}\n{post.text}\n\n"

        send_email(
            message,
            subject,
            recipient_email,
        )
