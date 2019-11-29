from django.db import models
from django.utils.translation import gettext as _

# Create your models here.



class Sighting(models.Model):
    latitude = models.DecimalField(max_digits=35, decimal_places=25)
    longitude = models.DecimalField(max_digits=35, decimal_places=25)

    unique_squirrel_id = models.SlugField(
        max_length=50,
        blank=True,
        default='',
        #unique=True,
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
            blank=True,
            #null=True,
            default='',
            )

    date = models.DateField('date sighted')

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
        max_length=255,
        blank=True,
        default = '',
     )

    running = models.BooleanField(null=True)
    chasing = models.BooleanField(null=True)
    climbing = models.BooleanField(null=True)
    eating = models.BooleanField(null=True)
    foraging = models.BooleanField(null=True)

    other_activities = models.TextField(
        #max_length=255,
        blank=True,
        default='',
        #unique=True,
     )

    kuks = models.BooleanField(null=True)
    quaas = models.BooleanField(null=True)
    moans = models.BooleanField(null=True)
    tail_flags = models.BooleanField(null=True)
    tail_twitches = models.BooleanField(null=True)
    approaches = models.BooleanField(null=True)
    indifferent = models.BooleanField(null=True)
    runs_from = models.BooleanField(null=True)

    def __str__(self):
        return self.unique_squirrel_id

