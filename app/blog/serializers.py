from rest_framework import serializers

from .models import Post, ReadStatus, Subscription


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["blog"]

    def create(self, validated_data):
        subscription = Subscription.objects.filter(
            subscriber=self.context["request"].user,
            blog=validated_data.get("blog"),
        )
        if subscription.exists():
            raise serializers.ValidationError("You are already subscribed to this blog")
        if self.context["request"].user == validated_data.get("blog").user:
            raise serializers.ValidationError("You can't subscribe to your own blog")
        return super().create(validated_data)


class SubscriptionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["blog"]


class ReadStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadStatus
        fields = ["post"]

    def create(self, validated_data):
        read_status = ReadStatus.objects.filter(
            user=self.context["request"].user,
            post=validated_data.get("post"),
        )
        if read_status.exists():
            raise serializers.ValidationError("You have already read this post")
        subscriber = Subscription.objects.filter(
            subscriber=self.context["request"].user,
            blog=validated_data.get("post").blog,
        )
        if not subscriber.exists():
            raise serializers.ValidationError("You are not subscribed to the blog")
        return super().create(validated_data)
