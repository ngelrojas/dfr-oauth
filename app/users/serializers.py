from rest_framework import serializers
from core.models.user import User


class UserSerializer(serializers.ModelSerializer):
    """user serializer"""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}
        read_only_fields = ("id",)

    def create(self, validate_data):
        """create user"""
        User.objects.create_user(**validate_data)
