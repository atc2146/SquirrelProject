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
    

    def __str__(self):
        return 'str defn'
    














