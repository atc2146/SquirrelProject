"""Class definition for SightingAdmin"""

from django.contrib import admin
from .models import Sighting

class SightingAdmin(admin.ModelAdmin):
    """Create a class to allow customization of the admin panel"""
    list_display = ('unique_squirrel_id', 'date')
    list_filter = ['date']
    search_fields = ['unique_squirrel_id']

admin.site.register(Sighting, SightingAdmin)
