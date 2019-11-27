from django.db import models
from django.utils.translation import gettext as _

# Create your models here.



class Sighting(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=20)
    longitude = models.DecimalField(max_digits=20, decimal_places=20)

    
    unique_squirrel_id = models.CharField(
        max_length=20,
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
            blank=True,
            #null=True,
            default='',
            )

    date = models.DateField('date sighted')
   
    age = models.IntegerField(max_length=3)

    primary_fur_color = models.CharField(
        max_length=20,
        unique=True,
     )

    location = models.CharField(
        max_length=20,
        unique=True,
     )

    specific_location = models.CharField(
        max_length=20,
        unique=True,
     )

    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()

    other_activites = models.CharField(
        max_length=20,
        unique=True,
     )

    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    
    tail_flags = models.CharField(
        max_length=20,
        unique=True,
     )

    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()

    runs_from = models.CharField(
        max_length=20,
        unique=True,
     )
    

    def __str__(self):
        return 'str defn'
    














