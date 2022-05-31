from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView

from users.forms import LoginForm, UserForm, EditUserForm
from users.models import User


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


class CreateUserView(LoginRequiredMixin, FormView):
    login_url = '/users/login/'
    form_class = UserForm
    template_name = 'users/signUp.html'
    success_url = '/users/home/'

    def form_valid(self, form):
        user = User.objects.create(username=self.request.POST['username'],
                                   git_access_token=self.request.POST['git_access_token'],
                                   email=self.request.POST['email'])
        user.set_password(self.request.POST['password'])
        user.save()
        return super().form_valid(form)


class EditUserView(LoginRequiredMixin, FormView):
    login_url = '/users/login/'
    form_class = EditUserForm
    template_name = 'users/signUp.html'
    success_url = '/users/home/'

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            'password': self.request.user.password,
            'git_access_token': self.request.user.git_access_token,
            'email': self.request.user.email
        })
        return initial

    def form_valid(self, form):
        user = self.request.user
        user.git_access_token = self.request.POST['git_access_token']
        user.email = self.request.POST['email']

        user.set_password(self.request.POST['password'])
        user.save()

        login(self.request, user)
        return super().form_valid(form)


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/users/login/'
    template_name = 'users/home.html'
