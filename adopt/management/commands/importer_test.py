import csv

from django.core.management.base import BaseCommand, CommandError
from adopt.models import SquirrelTest


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

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
                shift = item['Shift']
                date = item['Date']
                hectare_sq = int(item['Hectare Squirrel Number'])
                age = item['Age']
                primary_fur = item['Primary Fur Color']
                highlight_fur = item['Highlight Fur Color']
                combi_fur = item['Combination of Primary and Highlight Color']
                color_note = item['Color notes']
                location = item['Location']
                above_ground = item['Above Ground Sighter Measurement']
                spec_loc = item['Specific Location']
                running = True
                if item['Running']=='FALSE':
                    running = False
                chasing = True
                if item['Chasing']=='FALSE':
                    chasing = False
                climbing = True
                if item['Climbing']=='FALSE':
                    climbing = False
                eating = True
                if item['Eating']=='FALSE':
                    eating = False
                foraging = True
                if item['Foraging']=='FALSE':
                    foraging = False

                other_act = item['Other Activities']

                kuks = True
                if item['Kuks']=='FALSE':
                    kuks = False
                quaas = True
                if item['Quaas']=='FALSE':
                    quaas = False
                moans = True
                if item['Moans']=='FALSE':
                    moans = False
                flags = True
                if item['Tail flags']=='FALSE':
                    flags = False
                twitches = True
                if item['Tail twitches']=='FALSE':
                    twitches = False
                approaches = True
                if item['Approaches']=='FALSE':
                    approaches = False
                indifferent = True
                if item['Indifferent']=='FALSE':
                    indifferent = False
                runsfrom = True
                if item['Runs from']=='FALSE':
                    runsfrom = False


                other_int = item['Other Interactions'] 
                lat_long = item['Lat/Long']


                squirreltest = SquirrelTest.objects.create_squirreltest(x, y, unique_squirrel_id, hectare, shift, date, hectare_sq, age, primary_fur, highlight_fur,
                        combi_fur, color_note, location, above_ground, spec_loc, running, chasing, climbing, eating, foraging, other_act, kuks, quaas, moans, flags, twitches, approaches, indifferent, runsfrom, other_int, lat_long)
                squirreltest.save()

                self.stdout.write(self.style.SUCCESS('Successfully created squirrel "%s"' % unique_squirrel_id))







