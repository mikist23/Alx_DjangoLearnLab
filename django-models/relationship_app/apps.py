from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'


class YourAppConfig(AppConfig):
    name = 'yourapp'

    def ready(self):
        pass
        # import yourapp.signals