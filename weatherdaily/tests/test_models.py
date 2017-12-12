from django.test import TestCase
from weatherdaily.models import Weather


class WeatherModelTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        # set up objects to test data
        Weather.objects.create(email='test@test.com', location='Anchorage, AK')

    def test_email_label(self):
        weather = Weather.objects.get(id=1)
        field_label = weather._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_location_email(self):
        weather = Weather.objects.get(id=1)
        field_label = weather._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_location_max_length(self):
        weather = Weather.objects.get(id=1)
        max_length = weather._meta.get_field('location').max_length
        self.assertEquals(max_length, 50)
