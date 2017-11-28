from django.contrib import admin
from .models import Weather


class WeatherAdmin(admin.ModelAdmin):
    fields = ['email', 'location']
    list_display = ('email', 'location',)

admin.site.register(Weather, WeatherAdmin)
