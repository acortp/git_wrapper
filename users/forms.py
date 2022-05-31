from django import forms
from django.contrib.auth import authenticate

from users.models import User
from users.validators import unique_user


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


class UserForm(forms.ModelForm):
    username = forms.CharField(required=True, validators=[unique_user])
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'git_access_token']


class EditUserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password', 'email', 'git_access_token']