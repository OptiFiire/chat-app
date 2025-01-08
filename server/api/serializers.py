from rest_framework.serializers import ModelSerializer
from api.models import Message, Chat
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','name','avatar', 'biography', 'date_joined', 'last_login']


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
