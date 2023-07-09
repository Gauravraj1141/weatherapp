from django.contrib import admin

from .models import Weather

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    fields = [ 'temperature', 'pressure', 'humidity', 'wind', 'main_weather', 'weather', 'icon', 'time', 'city','lat','lon','created_at']
    

