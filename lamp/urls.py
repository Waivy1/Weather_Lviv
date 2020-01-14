from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index_page'),
    path('bulb/<str:state>', views.Bulb.as_view()),
    path('color/<int:r>/<int:g>/<int:b>', views.Color.as_view()),
    path('weather', views.Weather.as_view(), name='weather'),
]