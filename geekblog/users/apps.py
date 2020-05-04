from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "geekblog.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import geekblog.users.signals  # noqa F401
        except ImportError:
            pass
