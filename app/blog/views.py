from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Blog, Post, ReadStatus, Subscription
from .pagination import PostsPagination
from .serializers import (
    PostCreateSerializer,
    PostSerializer,
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
        blog = get_object_or_404(Blog, id=blog_id)
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
        post = get_object_or_404(Post, id=post_id)
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


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-created_at")
    permission_classes = [AllowAny]
    pagination_class = PostsPagination

    @extend_schema(
        summary="Retrieve [Post]",
        description="Retrieve all posts",
        responses={200: PostSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Create [Post]",
        description="Create new post",
        responses={201: PostCreateSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
