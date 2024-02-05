from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema

from .models import User
from .serializers import UserCreateSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    @extend_schema(
        summary="Create [User]",
        description="Create new user",
        responses={201: UserCreateSerializer()},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
