from django.apps import AppConfig


class EditorialprojectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EditorialProjects'

    def ready(self):
        import EditorialProjects.signals