from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ChatViewSet, DjoserUserViewSet

router = DefaultRouter()
router.register(r"users", DjoserUserViewSet, basename='user')
router.register(r"chats", ChatViewSet, basename='chat')
router.register(r"messages", MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls))
]
