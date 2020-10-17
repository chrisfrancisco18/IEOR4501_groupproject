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
                running = item['Running']
                chasing = item['Chasing']
                climbing = item['Climbing']
                eating = item['Eating']
                foraging = item['Foraging']
                other_act = item['Other Activities']
                kuks = item['Kuks']
                quaas = item['Quaas']
                moans = item['Moans']
                flags = item['Tail flags']
                twitches = item['Tail twitches']
                approaches = item['Approaches']
                indifferent = item['Indifferent']
                runsfrom = item['Runs from']
                other_int = item['Other Interactions']
                lat_long = item['Lat/Long']
                
                squirrel = Squirrel.objects.create_squirrel(x, y, unique_squirrel_id, hectare, shift, date,hectare_sq,
                           age, primary_fur,highlight_fur, combi_fur, color_note, location, above_ground, spec_loc, running,
                           chasing, climbing, eating, foraging, other_act, kuks, quaas, moans, flags, twitches, approaches,
                           indifferent, runsfrom, other_int, lat_long )
                squirrel.save()

                self.stdout.write(self.style.SUCCESS('Successfully created squirrel "%s"' % unique_squirrel_id))
