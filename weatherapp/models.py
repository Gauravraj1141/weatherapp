from django.db import models
from datetime import datetime


class Weather(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    temperature = models.IntegerField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    wind = models.IntegerField()
    main_weather = models.CharField(max_length=50)
    weather = models.CharField(max_length=50)
    icon = models.CharField(max_length=12)
    time = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    lat = models.CharField(max_length=50,null=True)
    lon = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(default= datetime.now, null=True)

    def __str__(self) -> str:
        return str(self.city)


