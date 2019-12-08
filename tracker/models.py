"""Definition of Sighting model for storing squirrel sightings in db"""

from django.db import models
from django.urls import reverse
#from django.forms import ModelForm
from django.utils.translation import gettext as _
from datetime import datetime, date
from django.core.exceptions import ValidationError
#from django.urls import reverse
#from .views import SightingIndexView

def validate_date(date):
    """Ensure date entered is valid and not in the future"""
    if date > date.today():
        raise ValidationError("Date cannot be in the past")


class Sighting(models.Model):
    """
    Sighting model for storing squirrel sightings information in db.

    **Model Fields**
    Latitude
    Longitude
    Unique Squirrel ID
    Shift
    Date
    Age
    Primary Fur Color
    Location
    Specific Location
    Running
    Chasing
    Climbing
    Eating
    Foraging
    Other Activities
    Kuks
    Quaas
    Moans
    Tail flags
    Tail twitches
    Approaches
    Indifferent
    Runs from

    """
    latitude = models.DecimalField(max_digits=35, decimal_places=25)
    longitude = models.DecimalField(max_digits=35, decimal_places=25)

    unique_squirrel_id = models.SlugField(
        max_length=50,
        blank=False,
        default='',
        unique=True,
     )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
     )

    shift = models.CharField(
            help_text=_('Time of sighting'),
            max_length=2,
            choices=SHIFT_CHOICES,
            blank=False,
            #null=True,
            default='',
            )

    date = models.DateField(
        help_text=_('date sighted'), 
        blank=False,
        default=None, 
        validators=[validate_date])

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
     )

    age = models.CharField(
            help_text=_('Age of squirrel'),
            max_length=10,
            choices=AGE_CHOICES,
            blank=True,
            default='',
            )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    PRIMARY_FUR_COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
     )

    primary_fur_color = models.CharField(
        help_text=_('Fur color of squirrel'),
        max_length=20,
        choices=PRIMARY_FUR_COLOR_CHOICES,
        blank=True,
        default = '',
        #unique=True,
     )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
     )

    location = models.CharField(
        help_text=_('Location of where the squirrel was when first sighted'),
        max_length=20,
        choices=LOCATION_CHOICES,
        blank=True,
        default = '',
     )

    specific_location = models.CharField(
        help_text=_('Specific location of the sighting'),
        max_length=255,
        blank=True,
        default = '',
     )

    running = models.BooleanField(help_text=_('Is the squirrel running?'), default=False)
    chasing = models.BooleanField(help_text=_('Is the squirrel chasing?'), default=False)
    climbing = models.BooleanField(help_text=_('Is the squirrel climbing?'), default=False)
    eating = models.BooleanField(help_text=_('Is the squirrel eating?'), default=False)
    foraging = models.BooleanField(help_text=_('Is the squirrel foraging?'), default=False)

    other_activities = models.TextField(
        help_text=_('What other activites is the squirrel doing?'),
        #max_length=255,
        blank=True,
        default='',
        #unique=True,
     )

    kuks = models.BooleanField(help_text=_('Is the squirrel kuking?'), default=False)
    quaas = models.BooleanField(help_text=_('Is the squirrel quaaing?'), default=False)
    moans = models.BooleanField(help_text=_('Is the squirrel moaning?'), default=False)
    tail_flags = models.BooleanField(help_text=_('Does the squirrel have a tail flag?'), default=False)
    tail_twitches = models.BooleanField(help_text=_('Is the squirrel\'s tail twitching?'), default=False)
    approaches = models.BooleanField(help_text=_('Did the squirrel approach you?'), default=False)
    indifferent = models.BooleanField(help_text=_('Was the squirrel indifferent to you?'), default=False)
    runs_from = models.BooleanField(help_text=_('Did the squirrel run from you?'), default=False)
    
    class Meta:
        get_latest_by = ['date']

    def __str__(self):
        return self.unique_squirrel_id

#    def get_absolute_url(self):
#        from django.urls import reverse
#        return reverse('SightingIndexView', args=[str(self.id)])

