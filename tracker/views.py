from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the trackers index.")

def map(request):
    return HttpResponse("Map view")

def add(request):
    return HttpResponse("add view")

def stats(request):
    return HttpResponse("stats view")

