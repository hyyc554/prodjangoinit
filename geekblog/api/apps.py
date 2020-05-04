from django.apps import AppConfig


# class ApiConfig(AppConfig):
#     name = 'api'
# from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApisConfig(AppConfig):
    name = "geekblog.api"
# /    verbose_name = _("Users")
#
#     def ready(self):
#         try:
#             import geekblog.users.signals  # noqa F401
#         except ImportError:
#             pass
