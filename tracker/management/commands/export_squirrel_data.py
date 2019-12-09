"""Definition of export_squirrel_data command line argument. Returns CSV of fields in db"""

import csv
import sys

from django.core.management.base import BaseCommand, CommandError

from tracker.models import Sighting

class Command(BaseCommand):
    """
    This command is used to export squirrel data in the db in CSV format to the path specified as the first argument of the command line function. 
    """
    help = 'Used to export squirrel sighting database (in csv format)'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path to be imported')
    
    def handle(self, *args, **kwargs):
        path = kwargs['file_path']
        field_names = [f.name for f in Sighting._meta.fields]
        
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(field_names) #write headers first
            for obj in Sighting.objects.all():
                writer.writerow(str(getattr(obj, field.name)) for field in Sighting._meta.fields)
                
        f.close() 
        self.stdout.write(f"CSV exported to {path}")
