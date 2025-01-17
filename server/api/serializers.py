from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from api.models import Message, Chat
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(ModelSerializer):
    id = CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "avatar",
            "biography",
            "date_joined",
            "last_login",
        ]


class MessageSerializer(ModelSerializer):
    id = CharField(read_only=True)
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ["id", "content", "is_read", "created_at", "sender"]


class ChatSerializer(ModelSerializer):
    id = CharField(read_only=True)
    last_message = SerializerMethodField()
    unread_messages_count = SerializerMethodField()
    partner = SerializerMethodField()

    class Meta:
        model = Chat
        fields = ["id", "partner", "last_message", "unread_messages_count"]

    def get_last_message(self, obj):
        last_message = obj.messages.order_by("-created_at").first()
        return MessageSerializer(last_message).data if last_message else None

    def get_unread_messages_count(self, obj):
        user = self.context["request"].user
        return obj.messages.filter(receiver=user, is_read=False).count()

    def get_partner(self, obj):
        user = self.context["request"].user
        other_user = obj.participants.exclude(id=user.id).first()
        return UserSerializer(other_user).data if other_user else None
