from django import forms

from users.models import User


class LoginForm(forms.Form):
    user = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'github_user']