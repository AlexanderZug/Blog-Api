from rest_framework import serializers

from .models import Post, Blog, Subscription


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
