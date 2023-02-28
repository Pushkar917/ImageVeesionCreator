from django.apps import AppConfig


class GlobalcontactdataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.globalContactData'

    def ready(self):
        import apps.globalContactData.signals
