from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView

from users.forms import LoginForm, SignUpForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/users/home/'

    def form_valid(self, form):
        user = authenticate(username=self.request.POST['user'],
                            password=self.request.POST['password'])

        login(self.request, user)
        return super().form_valid(form)

class LogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/users/login/')


class SignUpView(LoginRequiredMixin, FormView):
    login_url = '/users/login/'
    form_class = SignUpForm
    template_name = 'users/signUp.html'


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/users/login/'
    template_name = 'users/home.html'
