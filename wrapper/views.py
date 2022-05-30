from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from git import Repo

from wrapper import settings
from wrapper.forms import EditConfigForm
from wrapper.mixins import GetConfigMixin
from wrapper.utils import save_configuration


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
            remotes = []
            for remote in repo.remotes:
                can_create_pr = True
                for ref in remote.refs:
                    if settings.GIT_CONFIG['main_branch'] in ref.name.split('/'):
                        can_create_pr = False
                        break
                remotes.append({'info': remote, 'can_create_pr': can_create_pr})
            context_data.update({'repo': repo, 'remotes': remotes})
        else:
            context_data.update({'error': True, 'errorMsg': 'Could not load the repository'})
        return context_data
