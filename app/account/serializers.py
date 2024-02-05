import uuid

import mimesis
from rest_framework import serializers

from .models import User, VerifyToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
        ]


class VerifyTokenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyToken
        fields = ["first_name", "last_name", "email"]

    def create(self, validated_data):
        user, created = User.objects.get_or_create(email=validated_data.get("email"))
        if not created:
            raise serializers.ValidationError("This email is already in use.")

        if created:
            user.first_name = validated_data.get("first_name")
            user.last_name = validated_data.get("last_name")
            user.is_staff = False
            user.is_superuser = False
            user.save()

        verify_token = VerifyToken.objects.create(
            email=user.email,
            token=mimesis.Numeric().integer_number(10000, 50000),
            user=user,
            uuid=uuid.uuid4(),
        )
        return verify_token

    def to_representation(self, instance):
        return {
            "token": instance.token,
            "uuid": instance.uuid,
        }


class LoginUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyToken
        fields = ["token", "uuid"]

    def to_representation(self, instance):
        return {
            "id": instance.user.id,
            "first_name": instance.user.first_name,
            "last_name": instance.user.last_name,
        }


class SignViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "image",
            "email",
        ]
