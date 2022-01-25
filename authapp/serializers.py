from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import fields, serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        models = User
        fields = ('id', 'email', 'username', 'password', 'phone', 'first_name', 'last_name', 'locale')