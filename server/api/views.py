from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count, Max, Q
from api.models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from djoser import views as djoser_views


class DjoserUserViewSet(djoser_views.UserViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        chat = self.get_object()
        messages = chat.messages.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return (
            Chat.objects.filter(participants=self.request.user)
            .prefetch_related("messages__sender")
            .annotate(
                last_message_created_at=Max("messages__created_at"),
                unread_messages_count=Count(
                    "messages",
                    filter=Q(
                        messages__receiver=self.request.user, messages__is_read=False
                    ),
                ),
            )
        )


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
