from django.apps import AppConfig
from .db_listener import start_notification_listener


class DbNotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'db_notifications'

    # Launch database notification listener
    def ready(self):
        start_notification_listener()
        return super().ready()
