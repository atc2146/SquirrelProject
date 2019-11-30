from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from .models import Sighting

def index(request):
    return HttpResponse("Hello, world. You're at the trackers index.")

def map(request):
    template = loader.get_template('tracker/map.html')
    context = {}
    return HttpResponse(template.render(context, request))

def add(request):
    return HttpResponse("add view")

def stats(request):
    return HttpResponse("stats view")

def update(request, unique_squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
    return HttpResponse("Squirrel ID: " + str(squirrel))
