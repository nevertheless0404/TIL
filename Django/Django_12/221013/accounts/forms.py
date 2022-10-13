from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class UsersForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class kkUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")
