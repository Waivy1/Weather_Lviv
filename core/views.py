import random
import requests
import os


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View

WEATHER_API_TOKEN = os.environ.get('WEATHER_API_TOKEN')


class Bulb(View):
    def get(self, request, state):
        resp = requests.get(f'http://localhost/bulb/{state}')
        return JsonResponse({'state': state})


class IndexPage(View):
    def get(self, request):
        return render(request, 'index_page.html')


class Color(View):
    def get(self, request, r, g, b):
        color_resp = requests.get(f'http://localhost/set_color/{r}/{g}/{b}')
        return JsonResponse({'message': color_resp.text})


class Weather(View):
    def get(self, request):
        w_resp = requests.get(f'http://api.openweathermap.org/data/2.5/weather',
                              params={'q': 'Lviv',
                                      'APPID': WEATHER_API_TOKEN})

        weather_json = w_resp.json()
        print(weather_json)
        temp = round(weather_json['main']['temp'] / 60)
        sky_is = weather_json['weather'][0]['description']
        name = weather_json['name']
        return JsonResponse({'temp': temp, 'sky_is': sky_is, 'name': name})
