from django.contrib import admin
from weatherdaily import models


class WeatherAdmin(admin.ModelAdmin):
    fields = ['email', 'location']
    list_display = ('email', 'location')
    search_fields = ['email']
    list_filter = ['email']


class WeatherImageAdmin(admin.ModelAdmin):
    fields = ['weatherPic']
    search_fields = ['weatherPic']
    list_filter = ['weatherPic']
    list_display = ['weatherPic', 'weatherPic_height', 'weatherPic_width']
    list_editable = ['weatherPic_height', 'weatherPic_width']

admin.site.register(models.Weather, WeatherAdmin)
admin.site.register(models.WeatherImage, WeatherImageAdmin)




