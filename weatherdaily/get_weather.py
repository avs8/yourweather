from __future__ import absolute_import
import urllib2
import json
import os

from .models import *
from django.db.models import Q
from django.template.loader import get_template
from django.template import Context


from django.conf import settings
from django.core.mail import EmailMultiAlternatives

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yourweather.settings")


def get_image(weather, tem):

    weather = weather.lower()
    if weather in ['rain', 'scattered thunderstorms', 'showers', 'scattered showers', 'light rain']:
        pic = WeatherImage.objects.get(weatherPic="rain.jpg")
    elif weather in ['cloudy', 'overcast', 'chance of storm', 'mostly cloudy']:
        pic = WeatherImage.objects.get(weatherPic="cloudy.jpg")
    elif weather in ['partly cloudy']:
        pic = WeatherImage.objects.get(weatherPic="partlycloudy.jpg")
    elif weather in ['storm', 'chance of tstorm']:
        pic = WeatherImage.objects.get(weatherPic="rain.jpg")
    elif weather in ['light snow', 'icy', 'snow Showers', 'rain and snow']:
        pic = WeatherImage.objects.get(weatherPic="rain.jpg")
    elif weather in ['clear', 'sunny', 'partly sunny', 'mostly sunny'] and tem <= 50:
        pic = WeatherImage.objects.get(weatherPic="sunny.jpg")
    elif weather in ['clear', 'sunny', 'partly sunny', 'mostly sunny'] and tem >= 60:
        pic = WeatherImage.objects.get(weatherPic="sunny.jpg")
    else:
        pic = WeatherImage.objects.get(weatherPic="nice.jpg")
    return pic.weatherPic.name

def send_email():
    data = Weather.objects.all()
    locations = [i.encode("utf8").replace('\t', " ").split(',') for i in
                 Weather.objects.values_list('location', flat=True)]
    for i, v in enumerate(locations):
        location_city = '/' + locations[i][0].replace(' ', '_')
        location_state = locations[i][1].replace(' ', '_')
        url = 'http://api.wunderground.com/api/' + settings.WEATHER_API_KEY + '/geolookup/conditions/q/' + location_state + location_city + '.json'
        print (url)
        f = urllib2.urlopen(url)
        json_string = f.read()
        parsed_json = json.loads(json_string)
        city = parsed_json['location']['city']
        state = parsed_json['location']['state']
        weather = parsed_json['current_observation']['weather'].lower()
        real_temp = parsed_json['current_observation']['temperature_string']
        tem = float(real_temp[:4])
        if tem > 70:
            subject = "It's Going To Be " + weather.title() + " Today But Hot!"
        elif tem < 70 and tem > 50:
            subject = "It's Going To Be " + weather.title() + " Today But Warm!"
        elif tem < 50 and tem > 30:
            subject = "It's Going To Be " + weather.title() + " Today But Cold!"
        elif tem < 20:
            subject = "It's Going To Be " + weather.title() + " Today But Really Cold!"
        weather = parsed_json['current_observation']['weather']
        feelslike_string = parsed_json['current_observation']['feelslike_string']
        print weather
        image = get_image(weather, tem)
        print image
        image = 'http://127.0.0.1:8000/media/' + image
        print image
        email = (Weather.objects.get(Q(location__contains=city) & Q(email=data[i])))
        temp = get_template('weatherdaily/email.html')
        msg = EmailMultiAlternatives(subject, temp.render(Context({
            'city': city,
            'state': state,
            'weather': weather,
            'feelslike_string': feelslike_string,
            'real_temp': real_temp,
            'image': image
        })), settings.DEFAULT_FROM_EMAIL, [email])
        msg.attach_alternative(temp.render(Context({
            'city': city,
            'state': state,
            'weather': weather,
            'feelslike_string': feelslike_string,
            'real_temp': real_temp,
            'image': image
        })),    "text/html")
        msg.send()
