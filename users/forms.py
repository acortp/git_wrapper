from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from users.models import User


class LoginForm(forms.Form):
    user = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            return valid

        username = self.cleaned_data.get('user')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            self.add_error("user", 'Incorrect credentials')
            return False
        else:
            return True


class SignUpForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'git_access_token']