from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model with username and password fields for create API view"""

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
        )
