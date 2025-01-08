from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from django.db.models import Q
from django.db import models
import uuid


def random_uuid():
    return uuid.uuid4().int % (10**18)


class CustomUser(AbstractUser):
    id = models.BigIntegerField(
        unique=True, primary_key=True, default=random_uuid, editable=False
    )
    name = models.CharField(max_length=50, blank=False, default='User')
    username = models.CharField(max_length=20, unique=True, blank=False)
    avatar = models.ImageField(
        upload_to="images/avatars/",
        blank=True,
        null=True
    )
    biography = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    first_name = None
    last_name = None

    def __str__(self):
        return self.username


class Chat(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, default=random_uuid, editable=False)
    participants = models.ManyToManyField(to=CustomUser, related_name="participants")
    
    def __str__(self):
        first_participant = self.participants.first()
        last_participant = self.participants.last()
        return f"{first_participant} and {last_participant}"

class Message(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, default=random_uuid, editable=False)
    sender = models.ForeignKey(
        CustomUser, related_name="senders", on_delete=models.DO_NOTHING
    )
    receiver = models.ForeignKey(
        CustomUser, related_name="receivers", on_delete=models.DO_NOTHING
    )
    chat = models.ForeignKey(Chat, related_name="chats", on_delete=models.DO_NOTHING)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver}"
    
    def save(self, *args, **kwargs):
        if self.sender == self.receiver:
            raise ValidationError("Sender and receiver cannot be the same user.")
        
        chat = Chat.objects.filter(Q(participants=self.sender) & Q(participants=self.receiver)).first()
        if not chat:
            chat = Chat.objects.create()
            chat.participants.add(self.sender, self.receiver)
        
        self.chat = chat
        super().save(*args, **kwargs)
