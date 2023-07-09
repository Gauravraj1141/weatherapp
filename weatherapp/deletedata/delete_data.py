from apscheduler.schedulers.background import BackgroundScheduler
from weatherapp.models import Weather
from datetime import datetime, timedelta


def delete_weather_data():
    weather_data = Weather.objects.all()
    print("delte weather data called>>>>>>")

    for weather_detail in weather_data:
        created_time = weather_detail.created_at
        dt = datetime.fromisoformat(str(created_time))
        created_at = dt.time()

        # Convert to datetime object
        add_minute_dt = datetime.strptime(str(created_at), "%H:%M:%S.%f")

        # Add 20 minutes
        created_minute_dt = add_minute_dt + timedelta(minutes=20)
        after_20_min = created_minute_dt.time()

        # present time 
        present_dt = datetime.fromisoformat(str(datetime.now()))

        # Extract the time
        present_time = present_dt.strftime('%H:%M:%S.%f')

        if str(present_time) > str(after_20_min):
            try:
                weather_detail = Weather.objects.get(id=weather_detail.id)
                weather_detail.delete()
            except Exception as e:
                print(e)
  


# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(delete_weather_data , 'interval',seconds =2)
#     scheduler.start()



