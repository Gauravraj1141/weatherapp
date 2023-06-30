from django.shortcuts import render
import requests
from datetime import datetime
from .models import Weather

def ShowWeather(request):
        print(request.method)
        if request.method == "POST":
            lat = request.POST.get('lat')
            lon = request.POST.get('lon')

            url = "http://api.openweathermap.org/data/2.5/forecast"
            params = {
                "lat": lat,
                "lon": lon,
                "appid": "e78a372131b4e39a6dbce54cc156c407"
            }

            response = requests.get(url, params=params)
            weather_details = response.json()['list'][1]

            datetime_object = datetime.strptime(str(weather_details['dt_txt']), '%Y-%m-%d %H:%M:%S')

            # Extract the time component from the datetime object
            time = datetime_object.time()

            weather_data = {"temp":int((weather_details['main']['temp']) - 273.15),"pressure":weather_details['main']['pressure'],"Humidity":weather_details['main']['humidity'],"wind":round((weather_details['wind']['speed']*3.6),2),"weather":weather_details['weather'][0]['description'],"main_weather":weather_details['weather'][0]['main'],"icon":weather_details['weather'][0]['icon'],"time":time, "city":response.json()['city']['name']}

            # Adding data on database 

            data = Weather.objects.create(temperature = weather_data['temp'], pressure = weather_data['pressure'], humidity = weather_data['Humidity'], wind = weather_data['wind'], main_weather = weather_data['main_weather'], weather = weather_data['weather'], icon = weather_data['icon'] , time = weather_data['time'] , city = weather_data['city'], lat = lat, lon = lon)

            
            context = {"weather_data":weather_data}
            return render(request,'index.html',context)
        
        return render(request,'index.html')



