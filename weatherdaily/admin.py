from django.contrib import admin
from .models import Weather, WeatherImage


class WeatherAdmin(admin.ModelAdmin):
    fields = ['email', 'location']
    list_display = ('email', 'location')


class WeatherImageAdmin(admin.ModelAdmin):
    fields = ['weatherPic']

admin.site.register(Weather, WeatherAdmin)
admin.site.register(WeatherImage)




