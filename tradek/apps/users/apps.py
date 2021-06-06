from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tradek.apps.users'
    label = 'users'
    verbose_name = 'Users'


default_app_config = 'tradel.apps.users.UsersConfig'
