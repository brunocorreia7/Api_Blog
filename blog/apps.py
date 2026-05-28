from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # Importar o arquivo de signals garante que os@receiver sejam registrados
        import blog.signals

