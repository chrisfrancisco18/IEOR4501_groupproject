from django.core.management.base import BaseCommand
import csv

import Squirrel.models

class Command(BaseCommand):
    help = 'Fetch csv squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_data', help = 'file containing squirrel details')

    def handle(self, *args, **options):
        file_=options['squirrels_file']
        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                #assigning the read data to an each instance
                obj = Squirrel()
                obj.Latitude = item['X']
                obj.Longitude =item['Y']
                obj.Unique_Squirrel_ID =item['Unique Squirrel ID']
                obj.Hectare =item['Hectare']
                obj.Shift =item['Shift']
                obj.Date =item['Date']
                obj.Hectare_squirrel_nunber =item['Hectare Squirrel Number']
                obj.Age =item['Age']
                obj.Primary_Fur_Color =item['Primary Fur Color']
                obj.Highlight_Fur_Color =item['Highlight Fur Color']
                obj.Combi_Fur_Color =item['Combination of Primary and Highlight Color']
                obj.Color_Notes =item['Color notes']
                obj.Location =item['Location']
                obj.Above_Ground =item['Above Ground Sighter Measurement']
                obj.Specific_Location =item['Specific Location']
                obj.Running =item['Running']
                obj.Chasing =item['Chasing']
                obj.Climbing =item['Climbing']
                obj.Eating =item['Eating']
                obj.Foraging =item['Foraging']
                obj.Other_Activ =item['Other Activities']
                obj.Kuks =item['Kuks']
                obj.Quaas =item['Quaas']
                obj.Moans =item['Moans']
                obj.Tail_flags =item['Tail flags']
                obj.Tail_twitch =item['Tail twitches']
                obj.Approaches =item['Approaches']
                obj.Indifferent =item['Indifferent']
                obj.Runs_from =item['Runs from']
                obj.Other_Inter =item['Other Interactions']
                obj.Lat_Long  =item['Lat/Long']
                obj.save()
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCESS(msg))
