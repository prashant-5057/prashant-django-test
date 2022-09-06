from django.apps import AppConfig


class EventlistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventlist'
    def ready(self):
        import eventlist.signals