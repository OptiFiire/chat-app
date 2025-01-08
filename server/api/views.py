from rest_framework.viewsets import ModelViewSet
from api.models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from djoser import views as djoser_views

class DjoserUserViewSet(djoser_views.UserViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]   
    

class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
