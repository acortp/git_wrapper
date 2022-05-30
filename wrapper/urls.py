from django.urls import path

from wrapper.views import EditConfigView

urlpatterns = [
    path('configuration/', EditConfigView.as_view(), name='configuration'),
]