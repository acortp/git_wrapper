from django.urls import path

from users.views import LoginView, CreateUserView, HomeView, LogoutView, EditUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('edit_user/', EditUserView.as_view(), name='edit_user'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout')
]