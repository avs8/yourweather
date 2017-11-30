from django.contrib import admin
from .models import Weather, WeatherImage


class WeatherAdmin(admin.ModelAdmin):
    fields = ['email', 'location']
    list_display = ('email', 'location',)

admin.site.register(Weather, WeatherAdmin)
admin.site.register(WeatherImage)
