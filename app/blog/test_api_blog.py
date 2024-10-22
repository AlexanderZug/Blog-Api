import uuid

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Subscription


@pytest.fixture
def api_client():
    def _callable(user=None):
        client = APIClient()
        if user:
            client.force_authenticate(user=user)
        return client

    return _callable


@pytest.fixture
def authenticated_user(django_user_model):
    return django_user_model.objects.create_user(
        username=str(uuid.uuid4()),
        password=str(uuid.uuid4()),
        email="test@test.com",
    )


def test_subscription_create_view_success(django_user_model, api_client, authenticated_user):
    blog_author_2 = django_user_model.objects.create_user(
        username=str(uuid.uuid4()),
        password=str(uuid.uuid4()),
        email="test2@test.com",
    )
    url = reverse("subscription-create")
    data = {
        "blog": authenticated_user.blog.pk,
    }
    response = api_client(user=blog_author_2).post(url, data)

    assert response.status_code == status.HTTP_201_CREATED

    subscription = Subscription.objects.filter(
        subscriber=blog_author_2,
        blog=authenticated_user.blog,
    ).first()
    assert subscription is not None
    assert subscription.blog.pk == authenticated_user.blog.pk
    assert subscription.subscriber == blog_author_2
