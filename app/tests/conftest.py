import uuid

import pytest
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
def authenticated_user(django_user_model):
    return django_user_model.objects.create_user(
        username=str(uuid.uuid4()),
        password=str(uuid.uuid4()),
        email="test@test.com",
    )
