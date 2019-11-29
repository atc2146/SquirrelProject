from django.core.management.base import BaseCommand
from tracker.models import Sighting


import csv

class Command(BaseCommand):
    """
    This command is used to import squirrel data.
    """
    help = 'Used to import the data from the 2018 census file (in csv format)'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Indicated the file path to be imported')    

    def handle(self, *args, **kwargs):
        path = kwargs['file_path']
        self.stdout.write("File path: %s" % path)

    # FINISH WRITING THIS FUNCTION TO IMPLEMENT THE ACTION STUFF
    def handle2(self, *args, **kwargs):  
        path = kwargs['file_path']
        #Delete all previous from database
        Sighting.objects.all().delete()
        
        with open(path, newline='') as csv_file:
            my_reader = csv.reader(csv_file, delimiter='',quotechar='')
            for row in my_reader:
                Sighting.objects.create(
                        latitude=row[0],
                        longitude=row[2]
                        )
                count = count+1

        self.stdout.write("File path: %s" % path)
        self.stdout.write("rows inserted: %s " % count)

