import uuid

import pytest
from blog.models import Post, Subscription
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    def _callback(user=None):
        client = APIClient()
        if user:
            client.force_authenticate(user=user)
        return client

    return _callback


@pytest.fixture
def blog_author(django_user_model):
    return django_user_model.objects.create_user(
        username=str(uuid.uuid4()),
        password=str(uuid.uuid4()),
        email="test@test.com",
    )


@pytest.fixture
def subscriber(django_user_model):
    return django_user_model.objects.create_user(
        username=str(uuid.uuid4()),
        password=str(uuid.uuid4()),
        email="test2@test.com",
    )


@pytest.fixture
def subscription(blog_author, subscriber):
    return Subscription.objects.create(subscriber=subscriber, blog=blog_author.blog)


@pytest.fixture
def post(blog_author):
    return Post.objects.create(blog=blog_author.blog, title="Test title", text="Test text")
