from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from app.serializers import UserSerializer


class UserCreateView(CreateAPIView):
    """
    API to create a user instance with username and password fields
    """

    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
