from django.urls import path

from wrapper.views import EditConfigView, ViewRepoBranches, CreatePullRequestView

urlpatterns = [
    path('configuration/', EditConfigView.as_view(), name='configuration'),
    path('branches/', ViewRepoBranches.as_view(), name='branches'),
    path('create_pr/<str:branch_name>', CreatePullRequestView.as_view(), name='create_pr'),
    #path('edit_pr/<str:branch_name>', )
]