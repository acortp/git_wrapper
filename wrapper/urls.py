from django.urls import path

from wrapper.views import EditConfigView, ViewRepoBranches

urlpatterns = [
    path('configuration/', EditConfigView.as_view(), name='configuration'),
    path('remotes/', ViewRepoBranches.as_view(), name='remotes')
]