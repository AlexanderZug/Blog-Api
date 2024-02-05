from rest_framework import serializers

from .models import Post, Subscription


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
