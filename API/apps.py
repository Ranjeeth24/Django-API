from django.apps import AppConfig


class APIConfig(AppConfig):
    name = 'API'
    verbose_name = "API"
    default_app_config = 'API.apps.APIConfig'
