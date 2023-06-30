from django.apps import AppConfig


class WeatherappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weatherapp'

    def ready(self):
        print("start our sch suceefully..........")
        from .deletedata  import delete_data
        delete_data.start()