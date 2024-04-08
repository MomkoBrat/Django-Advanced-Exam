from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DjigitAuto.accounts'

    def ready(self):
        import DjigitAuto.accounts.signals
