from django.urls import path

from users.views import LoginView, SignUpView, HomeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home')
]