from rest_framework import serializers

from .models import Subscription


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
