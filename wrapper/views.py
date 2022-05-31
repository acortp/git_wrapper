import json
import requests

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from git import Repo

from wrapper import settings
from wrapper.forms import EditConfigForm, PullRequestForm
from wrapper.mixins import GetConfigMixin
from wrapper.models import PullRequest, PR_STATES
from wrapper.utils import save_configuration, set_errors_form

SSH_CMD = 'ssh -i id_deployment_key'

class EditConfigView(LoginRequiredMixin, GetConfigMixin, FormView):
    form_class = EditConfigForm
    login_url = "/users/login/"
    template_name = "wrapper/edit_config.html"
    success_url = "/users/home/"

    def get_initial(self):
        initial = super(EditConfigView, self).get_initial()
        initial.update(settings.GIT_CONFIG)
        return initial

    def form_valid(self, form):
        save_configuration(self.request.POST)
        return super().form_valid(form)


class ViewRepoBranches(LoginRequiredMixin, GetConfigMixin, TemplateView):
    login_url = '/users/login/'
    template_name = 'wrapper/repoBranchesDetail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()

        repo = Repo(settings.GIT_CONFIG['repo_path'])

        if not repo.bare:
            branches = []
            for branch in repo.branches:
                can_create_pr = True
                if settings.GIT_CONFIG['main_branch'] == branch.name:
                    can_create_pr = False
                branches.append({'info': branch, 'can_create_pr': can_create_pr})
            context_data.update({'repo': repo, 'branches': branches})
        else:
            context_data.update({'error': True, 'errorMsg': 'Could not load the repository'})
        return context_data


class CreatePullRequestView(LoginRequiredMixin, GetConfigMixin, FormView):
    form_class = PullRequestForm
    login_url = '/users/login/'
    template_name = 'wrapper/pull_request.html'
    success_url = '/wrapper/branches/'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data.update({
            'head': self.kwargs.get('branch_name'),
            'action': 'Create'
        })
        return context_data

    def form_valid(self, form):
        try:
            api = settings.GIT_CONFIG['api']
            repo_name = settings.GIT_CONFIG['repo_name']
            main_branch = settings.GIT_CONFIG['main_branch']
            git_token = self.request.user.git_access_token

            git_api = settings.GIT_CONFIG['git_pull_apis'][api]
            api_url = git_api.format(repo_name)

            headers = {
                "Authorization": "token {0}".format(git_token),
                "Content-Type": "application/json"}

            details = {
                'head': self.kwargs['branch_name'],
                'base': main_branch,
                'title': self.request.POST['title'],
                'body': self.request.POST['description']
            }

            git_request = requests.post(api_url, headers=headers, data=json.dumps(details))

            if not git_request.ok:
                set_errors_form(git_request, form)
                return self.form_invalid(form)

            pr_data = json.loads(git_request.text)

            pr = PullRequest.objects.create(
                title=self.request.POST['title'],
                description=self.request.POST['description'],
                user=self.request.user,
                main_branch=main_branch,
                head_branch=self.kwargs['branch_name'],
                link=pr_data.get('url'),
                git_id=pr_data.get('number'),
                state='open'
            )

            if self.request.POST['save_state'] == 'merge':
                merge_api = settings.GIT_CONFIG['merge_api']
                merge_url = merge_api.format(repo_name, pr.git_id)

                merge_details = {
                    'commit_title': self.request.POST['title'],
                    'commit_message': self.request.POST['description']
                }

                git_merge_request = requests.put(
                    merge_url,
                    headers=headers,
                    data=json.dumps(merge_details)
                )

                if not git_merge_request.ok:
                    form = set_errors_form(git_merge_request, form)
                    pr.state = 'merging'
                    pr.save()
                    return self.form_invalid(form)

                pr.state = 'merged'
                pr.save()

        except Exception as ex:
            form.add_error(None, ex.__str__())
            return super().form_invalid(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        kwargs = {"form": form}
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'head': self.kwargs.get('branch_name'),
            'action': 'Create'
        })
        return self.render_to_response(context_data)

