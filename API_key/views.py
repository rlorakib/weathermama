from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from API_key import weather_service


def index(request):
    cities=['Dhaka','Chittagong','Khulna','Islamabad','Kolkata','Delhi']
    return render(request,'index.html',context={
        'weather_updates':[weather_service.get_weather(city) for city in cities]

    })
