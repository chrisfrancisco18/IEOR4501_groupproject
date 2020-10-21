import csv
  
from django.core.management.base import BaseCommand, CommandError
from adopt.models import SquirrelTest

class Command(BaseCommand):
    help = 'Creates a csv file from internal squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)

    def squirrel_to_dict(self, squirrel):
        return {'X': squirrel.x, 'Y': squirrel.y, 'Unique Squirrel ID': squirrel.unique_squirrel_id,'Hectare': squirrel.hectare,
                'Shift': squirrel.shift, 'Date':squirrel.date, 'Hectare Squirrel Number': squirrel.hectare_sq, 'Age':squirrel.age,
                'Primary Fur Color':squirrel.primary_fur, 'Highlight Fur Color': squirrel.highlight_fur, 
                'Combination of Primary and Highlight Color': squirrel.combi_fur, 'Color notes':squirrel.color_note, 'Location':squirrel.location, 
                'Above Ground Sighter Measurement':squirrel.above_ground, 'Specific Location':squirrel.spec_loc, 'Running':squirrel.running, 
                'Chasing':squirrel.chasing,'Climbing':squirrel.climbing, 'Eating':squirrel.eating, 'Foraging':squirrel.foraging, 
                'Other Activities': squirrel.other_act, 'Kuks':squirrel.kuks, 'Quaas':squirrel.quaas, 'Moans':squirrel.moans, 'Tail flags':squirrel.flags,
                'Tail twitches':squirrel.twitches, 'Approaches':squirrel.approaches, 'Indifferent':squirrel.indifferent, 'Runs from': squirrel.runsfrom, 
                'Other Interactions':squirrel.other_int, 'Lat/Long':squirrel.lat_long
                }

    def handle(self, *args, **options):
        filename = options['csv_path'][0]

        queryset = SquirrelTest.objects.all()
        fieldnames = ['X', 'Y', 'Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color',
                'Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location','Above Ground Sighter Measurement','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions','Lat/Long'
                ]

        with open(filename, mode='w') as export_file:
            writer = csv.DictWriter(export_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for squirrel in queryset:
                writer.writerow(self.squirrel_to_dict(squirrel))
