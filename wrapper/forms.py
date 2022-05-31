from django import forms

from wrapper import settings
from wrapper.models import PullRequest
from wrapper.utils import get_api_choices


class EditConfigForm(forms.Form):
    repo_path = forms.CharField(required=True)
    api = forms.ChoiceField(required=True, choices=get_api_choices())
    project_name = forms.CharField(required=True)
    repo_name = forms.CharField(required=True)
    main_branch = forms.CharField(required=True)


class PullRequestForm(forms.ModelForm):
    save_state = forms.ChoiceField(required=True, choices=(('save', 'Only Save'), ('merge', 'Merge')))

    class Meta:
        model = PullRequest
        fields = ['title', 'description']