from django.shortcuts import render
from .forms import WeatherForm
from django.http import HttpResponse


def index(request):
    args = {}
    if request.POST:
        form = WeatherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks for submitting your information!!")
    else:
        form = WeatherForm()
        args = {}
    args['form'] = form

    return render(request, 'weatherdaily/index.html', args)


