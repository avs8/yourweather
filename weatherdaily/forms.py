from django.core.exceptions import ValidationError
from django import forms
from . models import Weather


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['email', 'location']

    def __init__(self, *args, **kwargs):
        super(WeatherForm, self).__init__(*args, **kwargs)
        self.fields['location'].queryset = Weather.objects.order_by('location')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = Weather.objects.filter(email=email).count()
        if email and exists > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if location is 'Where Do You Live?':
            raise ValidationError('Please select a valid location')
        return location
