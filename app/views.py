from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.generics import CreateAPIView


from app.serializers import UserSerializer


class UserCreateView(CreateAPIView):

    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
