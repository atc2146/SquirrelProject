from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Sighting
from .forms import SightingForm
# Create your views here


class SightingIndexView(generic.ListView):
    """
    Display all objects in :model:`tracker.Sighting`.

    **Context**

    ``sighting``
        An instance of :model:`tracker.Sighting`.

    **Template:**

    :template:`tracker/index.html`

    """
    model = Sighting
    paginate_by = 3500
    context_object_name = 'sightings'  # Default: object_list
    template_name = "tracker/index.html" # Default: <app_label>/<model_name>_list.html
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date')


def map(request):
    template = loader.get_template('tracker/map.html')
    sightings = Sighting.objects.all()[:100]
    context = {'sightings' : sightings,}
    return HttpResponse(template.render(context, request))


class SightingCreateView(generic.CreateView):
    template_name = 'tracker/add.html'
    form_class = SightingForm


class SightingUpdateView(generic.UpdateView):
    model = Sighting
    fields = '__all__'#('unique_squirrel_id',)
    template_name = 'tracker/update.html'
    slug_field = 'unique_squirrel_id'
    slug_url_kwarg = 'unique_squirrel_id'
    #success_url = reverse_lazy('tracker:index') #change
    context_object_name = 'sighting'

    def form_valid(self, form):
        if 'update_sighting' in self.request.POST:
            self.update_instance(form.cleaned_data)
            return super(SightingUpdateView,self).form_valid(form)
        elif 'delete_sighting' in self.request.POST:
            form.instance.delete()
            return HttpResponseRedirect(reverse('tracker:index', args=()))

    # user defined function
    def update_instance(self, valid_data):
        print(valid_data)
        pass
    



#rewrite this?
#use generic view?
def stats(request):
    """
    docstring to be completed
    """
    sightings_total = Sighting.objects.count()
    sightings_adult = Sighting.objects.filter(age='Adult').count()
    sightings_juvenile = Sighting.objects.filter(age='Juvenile').count()
    percent_adult = round(sightings_adult/sightings_total * 100)    
    percent_juvenile = round(sightings_juvenile/sightings_total * 100)
   
    # handle when nothing in db
    # if  no records  first() will return None, latest() will raise DoesNotExist exception
    latest_date = Sighting.objects.order_by('date').latest('date').date
    earliest_date = Sighting.objects.order_by('date').earliest().date
    most_common_date_query = Sighting.objects.values('date').annotate(total=Count('date')).order_by('-total')[0]
    #most_common_date = Sighting.objects.annotate(c=Count('date')).order_by('-c')[:1]

    running_true = Sighting.objects.filter(running=True).count()
    running_false = Sighting.objects.filter(running=False).count()

    chasing_true = Sighting.objects.filter(chasing=True).count()
    chasing_false = Sighting.objects.filter(chasing=False).count()

    climbing_true = Sighting.objects.filter(climbing=True).count()
    climbing_false = Sighting.objects.filter(climbing=False).count()    


    context = {
                'sightings_total': sightings_total,
                'sightings_adult': sightings_adult,
                'sightings_juvenile': sightings_juvenile,
                'percent_adult': percent_adult,
                'percent_juvenile': percent_juvenile,
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
    return render(request, 'tracker/stats.html', context)


