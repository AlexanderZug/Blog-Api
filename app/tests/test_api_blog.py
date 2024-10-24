import pytest
from blog.models import Post, Subscription
from django.urls import reverse
from rest_framework import status

pytestmark = [pytest.mark.django_db]


def test_not_authenticated_user_cannot_subscribe(api_client):
    url = reverse("subscription-create")
    data = {
        "blog": 1,
    }
    response = api_client().post(url, data)

    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_not_authenticated_user_can_read_posts(api_client):
    url = reverse("post-list")
    response = api_client().get(url)

    assert response.status_code == status.HTTP_200_OK


def test_not_authenticated_user_cannot_create_post(api_client):
    url = reverse("post-create")
    data = {
        "title": "Test title",
        "text": "Test text",
    }
    response = api_client().post(url, data)

    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_subscription_create_view_success(api_client, blog_author, subscriber):
    url = reverse("subscription-create")
    data = {
        "blog": blog_author.blog.pk,
    }
    response = api_client(user=subscriber).post(url, data)

    assert response.status_code == status.HTTP_201_CREATED

    sub = Subscription.objects.get(
        subscriber=subscriber,
        blog=blog_author.blog,
    )
    assert sub is not None
    assert sub.blog.pk == blog_author.blog.pk
    assert sub.subscriber == subscriber


def test_subscription_already_exists(api_client, blog_author, subscriber, subscription):
    url = reverse("subscription-create")
    data = {
        "blog": blog_author.blog.pk,
    }

    response = api_client(user=subscriber).post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "You are already subscribed to this blog" in response.data


def test_cannot_subscribe_to_own_blog(api_client, blog_author):
    url = reverse("subscription-create")
    data = {
        "blog": blog_author.blog.pk,
    }

    response = api_client(user=blog_author).post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "You can't subscribe to your own blog" in response.data


def test_subscription_delete_view_success(api_client, blog_author, subscriber, subscription):
    url = reverse("unsubscribe-delete", kwargs={"pk": subscription.pk})
    response = api_client(user=subscriber).delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Subscription.objects.filter(pk=subscription.pk).exists() is False


def test_create_new_post(api_client, blog_author):
    url = reverse("post-create")
    data = {
        "title": "Test title",
        "text": "Test text",
    }
    response = api_client(user=blog_author).post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == data["title"]
    assert response.data["text"] == data["text"]

    assert Post.objects.filter(blog=blog_author.blog).exists()


def test_read_status_create_view_success(api_client, blog_author, subscriber, subscription, post):
    url = reverse("read-status-create")
    data = {
        "post": post.pk,
    }
    response = api_client(user=subscriber).post(url, data)

    assert response.status_code == status.HTTP_201_CREATED

    read_status = post.read_statuses.filter(user=subscriber).first()
    assert read_status is not None
    assert read_status.post.pk == post.pk
    assert read_status.user == subscriber


def test_user_has_read_post(api_client, blog_author, subscriber, subscription, post):
    post.read_statuses.create(user=subscriber)

    url = reverse("read-status-create")
    data = {
        "post": post.pk,
    }
    response = api_client(user=subscriber).post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "You have already read this post" in response.data


def test_user_is_not_subscribed_to_the_blog(api_client, blog_author, subscriber, post):
    url = reverse("read-status-create")
    data = {
        "post": post.pk,
    }
    response = api_client(user=subscriber).post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "You are not subscribed to the blog" in response.data
