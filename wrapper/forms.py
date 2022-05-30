from django import forms

from wrapper import settings


class EditConfigForm(forms.Form):
    repo_path = forms.CharField(required=True)
    api = forms.CharField(required=True, options=settings.GIT_CONFIG["git_pull_apis"])
    project_name = forms.CharField(required=True)
    repo_name = forms.CharField(required=True)