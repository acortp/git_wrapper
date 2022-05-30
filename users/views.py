from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from users.forms import LoginForm, SignUpForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'


class SignUpView(LoginRequiredMixin, FormView):
    login_url = '/users/login/'
    form_class = SignUpForm
    template_name = 'users/signUp.html'


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/users/login/'
    template_name = 'users/home.html'
