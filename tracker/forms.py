"""Definition of Sightings Form to add or update a squirrel sighting."""

from django import forms
from .models import Sighting

class SightingForm(forms.ModelForm):
    """Define Sightings Form fields and model."""
    class Meta:
        model = Sighting
        fields = ['latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age','primary_fur_color', 'location', 'specific_location', 'running', 'chasing', 'climbing', 'eating', 'foraging', 'other_activities', 'kuks', 'quaas', 'moans', 'tail_flags', 'tail_twitches', 'approaches', 'indifferent', 'runs_from']

