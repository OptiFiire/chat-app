from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ChatViewSet, DjoserUserViewSet

router = DefaultRouter()
router.register(r"users", DjoserUserViewSet)
router.register(r"chats", ChatViewSet)
router.register(r"messages", MessageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
