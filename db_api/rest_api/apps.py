from django.apps import AppConfig
from .api_db_queryer import set_connection


class RestApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rest_api'

    # Launch the database connection for rest api
    def ready(self):
        set_connection()
        return super().ready()
