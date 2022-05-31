from django import forms

from users.models import User


def unique_user(value):
    if User.objects.filter(username=value).exists():
        raise forms.ValidationError("User name is not available")