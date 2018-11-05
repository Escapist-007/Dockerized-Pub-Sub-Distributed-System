from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

import googlemaps
import requests as re
import json

import reverse_geocoder

from .models import PlaceWeather  # Importing model

# Create your views here.

def clientDirection(request):
    return render(request, 'WayPoints/clientDirection.html')


def singleMarker(request):
    return render(request, 'WayPoints/singleMarker.html')  # Just to show a single marker on the map

def stylishMap(request):
    return render(request, 'WayPoints/stylishMap.html')





