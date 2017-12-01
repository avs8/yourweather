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


# def get_image(feelslike_string):
#     images = {'cloudy': 'http://www.freeimageslive.com/galleries/nature/weather/pics/rain_clouds_162145.jpg',
#               'partlycloudy': 'http://www.freeimageslive.com/galleries/nature/weather/pics/rain_clouds_162145.jpg',
#               'cold': 'http://data.whicdn.com/images/18499845/56998751503531805_MHunGchK_c_large.jpg',
#               'snowy': 'http://www.freeimageslive.com/galleries/nature/weather/pics/ice_storm%20morning_228600.jpg',
#               'windy': 'http://www.freeimages.co.uk/galleries/nature/weather/slides/lakeside_winter_mist_207837.htm',
#               'rain':'http://www.freeimageslive.com/galleries/nature/weather/pics/rainy_day_wet_1013459.jpg',
#               'nice': 'http://www.freeimageslive.com/galleries/nature/weather/pics/rainbow_qheensland_5232088.jpg'}
#     if feelslike_string in ['rain', 'scattered thunderstorms', 'showers', 'scattered showers', 'light rain']:
#         pic = images['rain']
#     elif feelslike_string in ['cloudy', 'overcast', 'chance of storm', 'mostly cloudy']:
#         pic = images['cloudy']
#     elif feelslike_string in ['partly cloudy']:
#         pic = images['partlycloudy']
#     elif feelslike_string in ['storm', 'chance of tstorm']:
#         pic = images['windy']
#     elif feelslike_string in ['light snow', 'icy', 'snow Showers', 'rain and snow']:
#         pic = images['snowy']
#     elif feelslike_string in ['clear', 'sunny', 'partly sunny', 'mostly sunny'] and tem <= 50:
#         pic = images['cold']
#     elif feelslike_string in ['clear', 'sunny', 'partly sunny', 'mostly sunny'] and tem >= 60:
#         pic = images['nice']
#     else:
#         pic = images['nice']
#     return pic

def send_email():
    data = Weather.objects.all()
    images = WeatherImage.objects.all()
    image_url = images[0].get_absolute_image_url

    image = 'http://127.0.0.1:8000' + image_url

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
        feelslike_string = parsed_json['current_observation']['feelslike_string']
        image = image
        print image
        email = (Weather.objects.get(Q(location__contains=city) & Q(email=data[i])))
        temp = get_template('weatherdaily/email.html')
        msg = EmailMultiAlternatives(subject, temp.render(Context({
            'city': city,
            'state': state,
            'weather': weather,
            'real_temp': real_temp,
            'feelslike_string': feelslike_string,
            'image': image
        })), settings.DEFAULT_FROM_EMAIL, [email])
        msg.attach_alternative(temp.render(Context({
            'city': city,
            'state': state,
            'weather': weather,
            'real_temp': real_temp,
            'feelslike_string': feelslike_string,
            'image': image
        })),    "text/html")
        msg.send()
