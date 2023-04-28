from django.apps import AppConfig
from django.contrib.auth.backends import UserModel
from django.db.models.signals import pre_save


class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'
    label = 'apps'
