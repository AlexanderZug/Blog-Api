from rest_framework.generics import ListAPIView
from drf_spectacular.utils import extend_schema

from .models import Post
from .serializers import PostListSerializer


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

    @extend_schema(
        summary="List [Post]",
        description="List of all existed posts",
        responses={200: PostListSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
