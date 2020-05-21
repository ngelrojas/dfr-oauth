from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.models.user import User
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """create user view"""

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
