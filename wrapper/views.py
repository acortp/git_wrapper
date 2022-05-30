from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from wrapper import settings
from wrapper.forms import EditConfigForm
from wrapper.mixins import GetConfigMixin
from wrapper.utils import save_configuration


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