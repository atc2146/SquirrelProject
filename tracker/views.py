from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse


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

def update(request):
    return HttpResponse("update view")
