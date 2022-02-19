from django.apps import AppConfig


class TodousersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todoUsers'
    
    def ready(self) -> None:
        import todoUsers.signals