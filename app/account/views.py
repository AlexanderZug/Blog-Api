from blog.models import Post
from django.contrib.auth import get_user_model, login, logout
from django.middleware.csrf import get_token
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import VerifyToken
from .pagination import UserPostsPagination
from .serializers import (
    LoginUserCreateSerializer,
    SignViewSerializer,
    UserPostSerializer,
    UserRetrieveSerializer,
    UserSerializer,
    UserSubscriptionSerializer,
    VerifyTokenCreateSerializer,
)

User = get_user_model()


class SignView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SignViewSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return self.request.user

    @extend_schema(
        summary="Check Auth [User]",
        description="Check user authenticated or not",
        responses={
            202: OpenApiResponse(UserRetrieveSerializer, description="Authenticated"),
            401: OpenApiResponse(description="Not authenticated"),
        },
    )
    def get(self, request, *args, **kwargs):
        get_token(request)
        if not self.request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ["patch", "get", "delete"]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    @extend_schema(
        summary="Retrieve [User:self]",
        description="Check info about signed user",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update [User:self]",
        description="Update user info for signed user",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        summary="Delete [User:self]",
        description="Delete signed user's account",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def perform_destroy(self, instance):
        logout(self.request)
        instance.delete()


class VerifyTokenCreateView(CreateAPIView):
    queryset = VerifyToken.objects.all()
    serializer_class = VerifyTokenCreateSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Retrieve [VerifyToken]",
        description="Create a verify token",
        responses={
            201: OpenApiResponse(
                VerifyTokenCreateSerializer, description="Token created"
            ),
            400: OpenApiResponse(description="Invalid data"),
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SignInCreateView(CreateAPIView):
    queryset = VerifyToken.objects.all()
    serializer_class = LoginUserCreateSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Sign In [User]",
        description="Authorization with token",
        responses={
            201: OpenApiResponse(
                VerifyTokenCreateSerializer, description="Login success"
            ),
            401: OpenApiResponse(description="Invalid token"),
        },
    )
    def post(self, request, *args, **kwargs):
        uuid = self.request.data.get("uuid")
        token = self.request.data.get("token")
        verify_token = VerifyToken.objects.filter(uuid=uuid, token=token).first()

        if not verify_token:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )

        if verify_token.email_expired:
            return Response(
                {"error": "Token expired"}, status=status.HTTP_401_UNAUTHORIZED
            )

        login(
            self.request,
            verify_token.user,
            backend="django.contrib.auth.backends.ModelBackend",
        )
        verify_token.delete()
        return Response(
            LoginUserCreateSerializer(verify_token).data,
            status=status.HTTP_200_OK,
        )


class UserSubscriptionView(ListAPIView):
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.subscriptions.all()

    @extend_schema(
        summary="Retrieve [User:subscription]",
        description="Retrieve user's subscriptions",
        responses={200: UserSubscriptionSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserPostListView(ListAPIView):
    serializer_class = UserPostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = UserPostsPagination

    def get_queryset(self):
        subscriptions = self.request.user.subscriptions.all()
        posts = Post.objects.filter(blog__in=subscriptions.values("blog")).order_by(
            "-created_at"
        )
        return posts[:500]

    @extend_schema(
        summary="Retrieve [User:posts by subscription]",
        description="Retrieve user's posts by subscription",
        responses={200: UserPostSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
