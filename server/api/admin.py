from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm

from rest_framework.authtoken.models import TokenProxy
from rest_framework.authtoken.admin import TokenAdmin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django.contrib import admin

from .models import Message, Chat, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, ChatForm, MessageForm

admin.site.unregister(Group)
admin.site.unregister(TokenProxy)


class GroupAdmin(GroupAdmin, ModelAdmin):
    pass


class CustomUserAdmin(UserAdmin, ModelAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    change_password_form = AdminPasswordChangeForm
    form = CustomUserChangeForm
    search_fields = ["username", "email", "name"]
    list_display = ["username", "email", "name", "is_staff"]

    fieldsets = (
        ("Profile", {"fields": ("name", "avatar", "biography")}),
        ("Account", {"fields": ("username", "email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "avatar",
                    "biography",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


class MessageAdmin(ModelAdmin):
    list_display = ["sender", "receiver", "is_read", "created_at"] + ["short_content"]
    readonly_fields = ["id", "created_at"]
    form = MessageForm
    search_fields = ["short_content"]

    def short_content(self, obj):
        return obj.content[:10] + "..." if len(obj.content) > 10 else obj.content

    short_content.short_description = "Content"


class ChatAdmin(ModelAdmin):
    list_display = ("display_participants",)
    form = ChatForm
    readonly_fields = ("id",)

    def display_participants(self, obj):
        first_participant = obj.participants.first()
        last_participant = obj.participants.last()
        return f"{first_participant} - {last_participant}"

    display_participants.short_description = "Participants"


class TokenAdmin(TokenAdmin, ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(TokenProxy, TokenAdmin)
