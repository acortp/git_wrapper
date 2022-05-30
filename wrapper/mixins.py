from wrapper import settings
from wrapper.utils import get_configuration


class GetConfigMixin:
    def dispatch(self, request, *args, **kwargs):
        config = get_configuration()
        settings.GIT_CONFIG = config
        return super().dispatch(request, *args, **kwargs)