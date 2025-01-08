from unfold.forms import UserCreationForm, UserChangeForm
from rest_framework.authtoken.models import Token
from .models import Chat, CustomUser, Message
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "name",
            "username",
            "email",
            "password1",
            "password2",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            "name",
            "username",
            "email",
            "password",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
        ]


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = "__all__"

    def clean_participants(self):
        participants = self.cleaned_data["participants"]
        if participants.count() != 2:
            raise forms.ValidationError("Chat must have exactly 2 participants.")
        return participants


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ["user"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["sender", "receiver", "content", "is_read"]

    def clean_sender(self):
        cleaned_data = super().clean()
        receiver = cleaned_data.get("receiver")
        sender = cleaned_data.get("sender")

        if sender == receiver:
            raise forms.ValidationError("Sender and receiver cannot be the same user.")
        return sender
