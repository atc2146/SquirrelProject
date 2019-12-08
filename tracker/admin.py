"""Class definition for Sighting Admin"""

from django.contrib import admin
from .models import Sighting


class SightingAdmin(admin.ModelAdmin):
    list_display = ('unique_squirrel_id', 'date')
    list_filter = ['date']
    search_fields = ['unique_squirrel_id']



admin.site.register(Sighting, SightingAdmin)
