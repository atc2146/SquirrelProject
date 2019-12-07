from django.core.management.base import BaseCommand, CommandError
from tracker.models import Sighting
import csv
import sys

class Command(BaseCommand):
    """
    This command is used to export squirrel data.
    """
    help = 'Used to export squirrel sighting database (in csv format)'
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path to be imported')
    
    def handle(self, *args, **kwargs):
        path = kwargs['file_path']
        field_names = [f.name for f in Sighting._meta.fields]
        
        with open(path, 'w') as f:
            writer = csv.writer(f)
            #write header first
            writer.writerow(field_names)
            
            for obj in Sighting.objects.all():
                writer.writerow(str(getattr(obj, field.name)) for field in Sighting._meta.fields)
                
        f.close()
        
        self.stdout.write(f"CSV exported to {path}")
