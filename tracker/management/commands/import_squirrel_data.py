from django.core.management.base import BaseCommand
from tracker.models import Sighting
from datetime import datetime

import csv

class Command(BaseCommand):
    """
    This command is used to import squirrel data.
    """
    help = 'Used to import the data from the 2018 census file (in csv format)'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path to be imported')

    #def handle(self, *args, **kwargs):
    #    path = kwargs['file_path']
    #    self.stdout.write("File path: %s" % path)

    # FINISH WRITING THIS FUNCTION TO IMPLEMENT THE ACTION STUFF
    def handle(self, *args, **kwargs):
        count=0
        path = kwargs['file_path']
        #Delete all previous from database
        Sighting.objects.all().delete()

        with open(path, newline='') as csv_file:
            my_reader = csv.DictReader(csv_file,
                    fieldnames=('X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color','Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location','Above Ground Sighter Measurement','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions','Lat Long','Zip Codes','Community Districts','Borough Boundaries','City Council Districts',  'Police Precincts'))
            headers=next(my_reader)
            for row in my_reader:

                date_formatted=datetime.strptime(row['Date'], '%m%d%Y').date()

                Sighting.objects.create(
                        latitude=row['Y'],
                        longitude=row['X'],
                        unique_squirrel_id=row['Unique Squirrel ID'],
                        shift=row['Shift'],

                        date=date_formatted,

                        age=row['Age'],
                        primary_fur_color=row['Primary Fur Color'],
                        location=row['Location'],
                        specific_location=row['Specific Location'],
                        running=convert_boolean(row['Running']),
                        chasing=convert_boolean(row['Chasing']),
                        climbing=convert_boolean(row['Climbing']),
                        eating=convert_boolean(row['Eating']),
                        foraging=convert_boolean(row['Foraging']),
                        other_activities=row['Other Activities'],
                        kuks=convert_boolean(row['Kuks']),
                        quaas=convert_boolean(row['Quaas']),
                        moans=convert_boolean(row['Moans']),
                        tail_flags=convert_boolean(row['Tail flags']),
                        tail_twitches=convert_boolean(row['Tail twitches']),
                        approaches=convert_boolean(row['Approaches']),
                        indifferent=convert_boolean(row['Indifferent']),
                        runs_from=convert_boolean(row['Runs from'])
                        )
                count = count+1

        self.stdout.write("File path: %s" % path)
        self.stdout.write("rows inserted: %s " % count)


def convert_boolean(string):
	"""
	Takes a string and returns a boolean representation
	"""
	if(string.lower()=="true"):
		return True
	else:
		return False	
