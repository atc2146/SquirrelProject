from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Sighting
from .forms import SightingForm
from django.urls import reverse


def index(request):
    squirrels = Sighting.objects.order_by('date')[:20]
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'tracker/index.html', context)

def map(request):
    template = loader.get_template('tracker/map.html')
    context = {}
    return HttpResponse(template.render(context, request))

def add(request):
    """
    DOCSTRING TO BE FILLED
    """
    if request.method == "POST":
        form = SightingForm(request.POST)
        try:
            if form.is_valid():
                sighting = form.save()
        except KeyError:
        # Redisplay the add form
            return render(request, 'tracker/add.html',{
                'form': form,
                'error_message': "Error occured while adding sighting",
                })
        else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
            return HttpResponseRedirect(reverse('tracker:update', args=(sighting.unique_squirrel_id,)))

    else:     
        form = SightingForm()    
    return render(request, 'tracker/add.html', {'form': form,})


def stats(request):
    """
    docstring to be completed
    """
    sightings_total = Sighting.objects.count()
    sightings_adult = Sighting.objects.filter(age='Adult').count()
    #percent_adult = round(sightings_adult/sightings_total * 100)    
    
    context = {
                'sightings_total': sightings_total,
                'sightings_adult': sightings_adult,
               # 'percent_adult': percent_adult,
            }
    return render(request, 'tracker/stats.html', context)




def update(request, unique_squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
    return HttpResponse("Squirrel ID: " + str(squirrel))
