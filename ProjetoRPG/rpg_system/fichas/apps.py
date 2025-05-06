from django.apps import AppConfig

class FichasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fichas'

    def ready(self):
        import fichas.signals  # Importa os sinais para que sejam registrados
