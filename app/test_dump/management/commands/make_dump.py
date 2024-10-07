import random
from datetime import timedelta

import mimesis
from blog.models import Post, ReadStatus, Subscription
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

User = get_user_model()


class Command(BaseCommand):
    help = "Generate test data for blog models"

    def handle(self, *args, **kwargs):
        users = []
        num_users_to_generate = 100
        num_posts_per_user = 5
        for _ in range(num_users_to_generate):
            user = User.objects.create(
                first_name=mimesis.Person().first_name(),
                last_name=mimesis.Person().surname(),
                username=mimesis.Person().username(),
                email=mimesis.Person().email(),
            )
            users.append(user)

        for user in users:
            for _ in range(num_posts_per_user):
                title = f"Post Title {random.randint(1, 100)}"
                text = f"Post Text {random.randint(1, 100)}"
                created_at = timezone.now() - timedelta(days=random.randint(1, 365))
                if hasattr(user, "blog"):
                    Post.objects.create(
                        title=title,
                        text=text,
                        created_at=created_at,
                        blog=user.blog,
                    )

            other_users = [u for u in users if u != user]
            num_subscriptions = random.randint(1, 5)
            for _ in range(num_subscriptions):
                subscriber = random.choice(other_users)
                if hasattr(user, "blog"):
                    Subscription.objects.create(subscriber=subscriber, blog=user.blog)

        for user in users:
            subscriptions = Subscription.objects.filter(subscriber=user)
            for subscription in subscriptions:
                posts = Post.objects.filter(blog=subscription.blog)
                for post in posts:
                    if random.random() < 0.5:
                        ReadStatus.objects.create(user=user, post=post, is_read=True)
        self.stdout.write(self.style.SUCCESS("Test data generation completed successfully"))
