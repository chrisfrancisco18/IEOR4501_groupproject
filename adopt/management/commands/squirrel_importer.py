import csv
from django.core.management.base import BaseCommand, CommandError
from adopt.models import Squirrel
class Command(BaseCommand):
    help = 'Pulling csv squirrel data'
    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)
    def handle(self, *args, **options):
        filename = options['csv_path'][0]
        with open(filename) as f:
            reader = csv.DictReader(f)
            for item in reader:
                x = item['X']
                y = item['Y']
                unique_squirrel_id = item['Unique Squirrel ID']
                hectare = item['Hectare']
                shift= item['Shift']
                date = item['Date']
                hectare_sq = item['Hectare Squirrel Number']
                age = item['Age']
                primary_fur = item['Primary Fur Color']
                highlight_fur = item['Highlight Fur Color']
                combi_fur = item['Combination of Primary and Highlight Color']
                color_note = item['Color notes']
                location = item['Location']
                above_ground = item['Above Ground Sighter Measurement']
                spec_loc = item['Specific Location']

                running = True
                if item['Running']=="FALSE":
                    running = False
                if item['Running']=="TRUE":
                    running = True
                
                chasing = True
                if item['Chasing']=="FALSE":
                    chasing = False
                if item['Chasing']=="TRUE":
                    chasing = True
                
                climbing = True
                if item['Climbing']=="FALSE":
                    climbing = False
                if item['Climbing']=="TRUE":
                    climbing = True
                
                eating = True
                if item['Eating']=="FALSE":
                    eating = False
                if item['Eating']=="TRUE":
                    eating = True
                
                foraging = True
                if item['Foraging']=="FALSE":
                    foraging = False
                if item['Foraging']=="TRUE":
                    foraging = True
        
                other_act = item['Other Activities']
                
                kuks=True
                if item['Kuks']=="FALSE":
                    kuks = False
                if item['Kuks']=="TRUE":
                    kuks  = True
                
                quaas= True
                if item['Quaas']=="FALSE":
                    quaas = False
                if item['Quaas']=="TRUE":
                    quaas = True
                
                moans= True
                if item['Moans']=="FALSE":
                    moans = False
                if item['Moans']=="TRUE":
                    moans = True
                
                flags = True
                if item['Tail flags']=="FALSE":
                    flags = False
                if item['Tail flags']=="TRUE":
                    flags = True
                
                twitches = True
                if item['Tail twitches']=="FALSE":
                    twitches = False
                if item['Tail twitches']=="TRUE":
                    twitches = True
            
                approaches = True
                if item['Approaches']=="FALSE":
                    approaches = False
                if item['Approaches']=="TRUE":
                    approaches = True
                
                indifferent = True
                if item['Indifferent']=="FALSE":
                    indifferent = False
                if item['Indifferent']=="TRUE":
                    indifferent = True
                
                runsfrom = True
                if item['Runs from']=="FALSE":
                    runsfrom = False
                if item['Runs from']=="TRUE":
                    runsfrom = True
    
                other_int = item['Other Interactions']
                lat_long = item['Lat/Long']
                
                squirrel = Squirrel.objects.create_squirrel(x, y, unique_squirrel_id, hectare, shift, date,hectare_sq,
                           age, primary_fur,highlight_fur, combi_fur, color_note, location, above_ground, spec_loc, running,
                           chasing, climbing, eating, foraging, other_act, kuks, quaas, moans, flags, twitches, approaches,
                           indifferent, runsfrom, other_int, lat_long )
                squirrel.save()

                self.stdout.write(self.style.SUCCESS('Successfully created squirrel "%s"' % unique_squirrel_id))
