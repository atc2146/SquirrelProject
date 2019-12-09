"""Definitions of Django views for handling web requests."""

from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import SightingForm
from .models import Sighting


class SightingIndexView(generic.ListView):
    """
    Display all objects in :model:`tracker.Sighting`.

    **Context**

    ``sighting``
        An instance of :model:`tracker.Sighting`.

    **Template:**

    :template:`tracker/index.html`

    """
    # Default: <app_label>/<model_name>_list.html
    template_name = 'tracker/index.html'
    paginate_by = 3500
    # Specifying the queryset is the same as specyfying the model
    queryset = Sighting.objects.order_by('-date')
    

def map(request):
    """Renders web request from diplaying map and squirrel sightings"""
    sightings = Sighting.objects.all()[:100]
    context = {
        'sightings' : sightings,
        }
    return render(request, 'tracker/map.html', context)


class SightingCreateView(generic.CreateView):
    """Renders web request for creating a new squirrel sighting"""
    template_name = 'tracker/add.html'
    form_class = SightingForm
    def get_success_url(self):
        return reverse('tracker:index')


class SightingUpdateView(generic.UpdateView):
    """Handle web requests for updating the Sightings View"""
    model = Sighting
    fields = '__all__'
    template_name = 'tracker/update.html'
    slug_field = 'unique_squirrel_id'
    slug_url_kwarg = 'unique_squirrel_id'
    success_url = reverse_lazy('tracker:index')

    def form_valid(self, form):
        """If the form is valid"""
        return super(SightingUpdateView, self).form_valid(form)


def stats(request):
    """Handle display of sighting statistics."""

    # handle when nothing in db
    try:
        sightings_total = Sighting.objects.count()
        sightings_adult = Sighting.objects.filter(age='Adult').count()
        sightings_juvenile = Sighting.objects.filter(age='Juvenile').count()        
        most_common_date_query = Sighting.objects.values('date').annotate(total=Count('date')).order_by('-total')[0]
        latest_date = Sighting.objects.order_by('date').latest('date').date
        earliest_date = Sighting.objects.order_by('date').earliest().date
        running_true = Sighting.objects.filter(running=True).count()
        running_false = Sighting.objects.filter(running=False).count()
        chasing_true = Sighting.objects.filter(chasing=True).count()
        chasing_false = Sighting.objects.filter(chasing=False).count()
        climbing_true = Sighting.objects.filter(climbing=True).count()
        climbing_false = Sighting.objects.filter(climbing=False).count()    
        has_no_sightings = False
        context = {
                'has_no_sightings': has_no_sightings,
                'sightings_total': sightings_total,
                'sightings_adult': sightings_adult,
                'sightings_juvenile': sightings_juvenile,
                'latest_date': latest_date,
                'earliest_date': earliest_date,
                'most_common_date': most_common_date_query['date'],
                'most_common_date_count': most_common_date_query['total'],
                'running_true': running_true,
                'running_false': running_false,
                'chasing_true': chasing_true,
                'chasing_false': chasing_false,
                'climbing_true': climbing_true,
                'climbing_false': climbing_false,
            }   
    except Exception as e:
        print('No records in database:\n' + str(e))
        has_no_sightings = True
        context = {
                'has_no_sightings': has_no_sightings,
            }
    
    return render(request, 'tracker/stats.html', context)


