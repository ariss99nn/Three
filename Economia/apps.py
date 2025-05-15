from django.apps import AppConfig


class EconomiaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Economia'

    def ready(self):
        import Economia.signals
