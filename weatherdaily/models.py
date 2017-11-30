# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.conf import settings

ADDRESS_CHOICES = (
 ('Where Do You Live?', 'Where Do You Live?'),
 ('Albuquerque, New Mexico', 'Albuquerque, NM'),
 ('Anaheim, California', 'Anaheim, CA'),
 ('Anchorage, Alaska', 'Anchorage, AK'),
 ('Arlington, Texas', 'Arlington, TX'),
 ('Atlanta, Georgia', 'Atlanta, GA'),
 ('Aurora, Colorado', 'Aurora, CO'),
 ('Austin, Texas', 'Austin, TX'),
 ('Bakersfield, California', 'Bakersfield, CA'),
 ('Baltimore, Maryland', 'Baltimore, MD'),
 ('Baton Rouge, Louisiana', 'Baton Rouge, LA'),
 ('Boise, Idaho', 'Boise, ID'),
 ('Boston, Massachusetts', 'Boston, MA'),
 ('Buffalo, New York', 'Buffalo, NY'),
 ('Chandler, Arizona', 'Chandler, AR'),
 ('Charlotte, North Carolina', 'Charlotte, NC'),
 ('Chesapeake, Virginia', 'Chesapeake, VA'),
 ('Chicago, Illinois', 'Chicago, IL'),
 ('Chula Vista, California', 'Chula Vista, CA'),
 ('Cincinnati, Ohio', 'Cincinnati, OH'),
 ('Cleveland, Ohio', 'Cleveland, OH'),
 ('Colorado Springs, Colorado', 'Colorado Springs, CO'),
 ('Columbus, Ohio', 'Columbus, OH'),
 ('Corpus Christi, Texas', 'Corpus Christi, TX'),
 ('Dallas, Texas', 'Dallas, TX'),
 ('Denver, Colorado', 'Denver, CO'),
 ('Detroit, Michigan', 'Detroit, MI'),
 ('El Paso, Texas', 'El Paso, TX'),
 ('Fort Wayne, Indiana', 'Fort Wayne, IN'),
 ('Fort Worth, Texas', 'Fort Worth, TX'),
 ('Fremont, California', 'Fremont, CA'),
 ('Fresno, California', 'Fresno, CA'),
 ('Garland, Texas', 'Garland, TX'),
 ('Gilbert, Arizona', 'Gilbert, AR'),
 ('Glendale, Arizona', 'Glendale, AR'),
 ('Greensboro, North Carolina', 'Greensboro, NC'),
 ('Henderson, Nevada', 'Henderson, NV'),
 ('Hialeah, Florida', 'Hialeah, FL'),
 ('Honolulu, Hawai', 'Honolulu, HI'),
 ('Houston, Texas', 'Houston, Texas'),
 ('Indianapolis, Indiana', 'Indianapolis, IN'),
 ('Irvine, California', 'Irvine, CA'),
 ('Irving, Texas', 'Irving, Texas'),
 ('Jacksonville, Florida', 'Jacksonville, FL'),
 ('Jersey City, New Jersey', 'Jersey City, NJ'),
 ('Kansas City, Missouri', 'Kansas City, MO'),
 ('Laredo, Texas', 'Laredo, TX'),
 ('Las Vegas, Nevada', 'Las Vegas, NV'),
 ('Lexington, Kentucky', 'Lexington, KY'),
 ('Lincoln, Nebraska', 'Lincoln, NE'),
 ('Long Beach, California', 'Long Beach, CA'),
 ('Los Angeles, California', 'Los Angeles, CA'),
 ('Louisville, Kentucky', 'Louisville, KY'),
 ('Lubbock, Texas', 'Lubbock, TX'),
 ('Madison, Wisconsin', 'Madison, WI'),
 ('Memphis, Tennessee', 'Memphis, TN'),
 ('Mesa, Arizona', 'Mesa, AR'),
 ('Miami, Florida', 'Miami, FL'),
 ('Milwaukee, Wisconsin', 'Milwaukee, WI'),
 ('Minneapolis, Minnesota', 'Minneapolis, MN'),
 ('Nashville, Tennessee', 'Nashville, TN'),
 ('New Orleans, Louisiana', 'New Orleans, LA'),
 ('New York, New York', 'New York, NY'),
 ('Newark, New Jersey', 'Newark, NJ'),
 ('Norfolk, Virginia', 'Norfolk, VA'),
 ('North Las Vegas, Nevada', 'North Las Vegas, NV'),
 ('Oakland, California', 'Oakland, CA'),
 ('Oklahoma City, Oklahoma', 'Oklahoma City, OK'),
 ('Omaha, Nebraska', 'Omaha, NE'),
 ('Orlando, Florida', 'Orlando, FL'),
 ('Philadelphia, Pennsylvania', 'Philadelphia, PA'),
 ('Phoenix, Arizona', 'Phoenix, AZ'),
 ('Pittsburgh, Pennsylvania', 'Pittsburgh, PA'),
 ('Plano, Texas', 'Plano, TX'),
 ('Portland, Oregon', 'Portland, OR'),
 ('Raleigh, North Carolina', 'Raleigh, NC'),
 ('Reno, Nevada', 'Reno, NV'),
 ('Richmond, Virginia', 'Richmond, VA'),
 ('Riverside, California', 'Riverside, CA'),
 ('Sacramento, California', 'Sacramento, CA'),
 ('Saint Paul, Minnesota', 'Saint Paul, MN'),
 ('San Antonio, Texas', 'San Antonio, TX'),
 ('San Bernardino, California', 'San Bernardino, CA'),
 ('San Diego, California', 'San Diego, CA'),
 ('San Francisco, California', 'San Francisco, CA'),
 ('San Jose, California', 'San Jose, CA'),
 ('Santa Ana, California', 'Santa Ana, CA'),
 ('Scottsdale, Arizona', 'Scottsdale, AR'),
 ('Seattle, Washington', 'Seattle, WA'),
 ('St. Louis, Missouri', 'St. Louis, MO'),
 ('St. Petersburg, Florida', 'St. Petersburg, FL'),
 ('Stockton, California', 'Stockton, CA'),
 ('Tampa, Florida', 'Tampa, FL'),
 ('Toledo, Ohio', 'Toledo, OH'),
 ('Tucson, Arizona', 'Tucson, AR'),
 ('Tulsa, Oklahoma', 'Tulsa, OK'),
 ('Virginia Beach, Virginia', 'Virginia Beach, VA'),
 ('Washington, District of Columbia', 'Washington, DC'),
 ('Wichita, Kansas', 'Wichita, KS'),
 ('Winston Salem, North Carolina', 'Winston Salem, NC'))


class Weather(models.Model):
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=50, choices=ADDRESS_CHOICES, default='Where Do You Live?')

    class Meta:
        unique_together = ('email', 'location')

    def __str__(self):
        return self.email


def upload_location(obj, filename):
    return "%s%s" % (obj.id, filename)

class WeatherImage(models.Model):
    weatherPic = models.ImageField(upload_to=upload_location,
                                   null=True, blank=True,
                                   height_field='weatherPic_height',
                                   width_field='weatherPic_width')
    weatherPic_height = models.IntegerField(default=0)
    weatherPic_width= models.IntegerField(default=0)

    def __str__(self):
      return self.weatherPic.name

    @property
    def get_absolute_image_url(self):
      return '%s' % self.weatherPic.url
