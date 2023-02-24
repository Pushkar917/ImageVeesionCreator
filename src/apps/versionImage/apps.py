from django.apps import AppConfig


class VersionimageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.versionImage'

    def ready(self):
        import apps.versionImage.signals
