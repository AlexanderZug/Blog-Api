from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Blog, Post, ReadStatus, Subscription
from .serializers import (
    ReadStatusCreateSerializer,
    SubscriptionCreateSerializer,
    SubscriptionDeleteSerializer,
)


class SubscriptionCreateView(CreateAPIView):
    serializer_class = SubscriptionCreateSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        blog_id = self.request.data.get("blog")
        blog = Blog.objects.filter(id=blog_id).first()
        serializer.save(
            subscriber=self.request.user,
            blog=blog,
        )

    @extend_schema(
        summary="Create [Subscription]",
        description="Create new subscription",
        responses={201: SubscriptionCreateSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SubscriptionDeleteView(DestroyAPIView):
    serializer_class = SubscriptionDeleteSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Delete [Subscription]",
        description="Delete subscription",
        responses={204: SubscriptionDeleteSerializer},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ReadStatusCreateView(CreateAPIView):
    serializer_class = ReadStatusCreateSerializer
    queryset = ReadStatus.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get("post")
        post = Post.objects.filter(id=post_id).first()
        serializer.save(
            user=self.request.user,
            post=post,
        )

    @extend_schema(
        summary="Create [ReadStatus]",
        description="Create new read status",
        responses={201: ReadStatusCreateSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
