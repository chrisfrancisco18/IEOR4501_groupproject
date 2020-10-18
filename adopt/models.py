from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime

# Create your models here




class SquirrelManager(models.Manager):
    def create_squirrel(self, x, y, unique_squirrel_id, hectare, shift, date,hectare_sq, age, primary_fur,highlight_fur, combi_fur, color_note, location, above_ground, spec_loc, running, chasing, climbing, eating, foraging, other_act, kuks, quaas, moans, flags, twitches, approaches, indifferent, runsfrom, other_int, lat_long ):
        squirrel = self.create(x=x, y=y, unique_squirrel_id=unique_squirrel_id,hectare=hectare, shift=shift, date=date,hectare_sq=hectare_sq, age=age, primary_fur=primary_fur, highlight_fur=highlight_fur, combi_fur=combi_fur, color_note=color_note, location=location, above_ground=above_ground, spec_loc=spec_loc, running=running, chasing=chasing, climbing=climbing, eating=eating, foraging=foraging, other_act=other_act, kuks=kuks, quaas=quaas, moans=moans, flags=flags, twitches=twitches, approaches=approaches, indifferent=indifferent, runsfrom=runsfrom, other_int=other_int, lat_long=lat_long
)
        return squirrel

class Squirrel(models.Model):
    x = models.FloatField(default='0.00')
    y = models.FloatField(default='0.00')
    unique_squirrel_id = models.CharField(max_length=14, default='')
   # unique_squirrel_id=models.CharField(
   #    # primary_key=True,
   #     max_length=14,
   #     help_text=_("The Unique ID"),
   #     default=''
   # )
    
    hectare=models.CharField(
        blank=True,
        max_length=4,
        help_text=_("Hectare"),
        default='',
    )
    
   # AM = 'AM'
   # PM = 'PM'
    
   # SHIFT_CHOICES = [
   #     (AM, _('AM')),
   #     (PM, _('PM')),
   # ]
    
  #  Shift=models.CharField(
  #      max_length=3,
  #      choices=SHIFT_CHOICES,
  #      default=AM,
  #  )

    shift = models.CharField(
            max_length=3,
            default = '',
            )
    

 #   date=models.DateField(
 #       help_text=_("Date"),
 #       default=datetime.now,
 #   )
    date=models.CharField(
        max_length=9,
        help_text=_("Date"),
        default='',
     )
    
    hectare_sq=models.IntegerField(
       # blank=True,
        help_text=_("Hectare Number"),
        default=0,
    )
    
   # ADULT = 'Adult'
   # JUVENILE = 'Juvenile'
   # OTHER = ''
    
   # AGE_CHOICES = [
   #     (ADULT, _('Adult')),
   #     (JUVENILE, _('Juvenile')),
   #     (OTHER, _('')),
   # ]
    
    age=models.CharField(
       # blank=True,
        max_length=20,
        help_text=_("Age"),
       # choices=AGE_CHOICES,
        default='',
    )
    
    primary_fur=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Primary Fur Color"),
        default='',
    )
    
    highlight_fur=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Highlight Fur Color"),
        default='',
    )
    
    combi_fur=models.CharField(
        blank=True,
        max_length=40,
        help_text=_("Combine Fur Color"),
        default='',
    )
    
    color_note=models.CharField(
        blank=True,
        max_length=40,
        help_text=_("Color Note"),
        default='',
    )
    
   # AG = 'Above Ground'
   # GP = 'Ground Plane'
   # OTHER = ''
    
   # LOCATION_CHOICES = [
   #    (AG, _('Above Ground')),
   #     (GP, _('Ground Plane')),
   #     (OTHER, _('')),
   # ]
    
    location=models.CharField(
        max_length=20,
        help_text=_("Locations"),
       # choices=LOCATION_CHOICES,
        default='',
    )
    
    above_ground=models.CharField(
       # blank=True,
        max_length=20,
        default='',
       # help_text=_("How Far from Ground Please Put The Number. If Found On The Ground Please Put FALSE"),
    )
    
    spec_loc=models.CharField(
       # blank=True,
        max_length=70,
        default='',
       # help_text=_("Specific Location"),
    )
    
    running=models.BooleanField()
    chasing=models.BooleanField()
    climbing=models.BooleanField()
    eating=models.BooleanField()
    foraging=models.BooleanField()
    
    other_act=models.CharField(
       # blank=True,
        max_length = 30,
        default='',
       # help_text=_("Other Activites"),
    )
    
    kuks=models.BooleanField()
    quaas=models.BooleanField()
    moans=models.BooleanField()
    flags=models.BooleanField()
    twitches=models.BooleanField()
    approaches=models.BooleanField()
    indifferent=models.BooleanField()
    runsfrom=models.BooleanField()
    
    other_int=models.CharField(
        blank=True,
        max_length=20,
        default='',
       # help_text=_("Other Interactions"),
    )
    
    lat_long=models.CharField(
        blank=True,
        max_length=100,
    )
    
    def __str__(self):
        return self.Unique_Squirrel_ID


    objects = SquirrelManager()



class SquirrelTestManager(models.Manager):
    def create_squirreltest(self, x, y, unique_squirrel_id, hectare, shift, date, hectare_sq, age, primary_fur, highlight_fur,combi_fur, color_note, location, above_ground, spec_loc, running, chasing, climbing, eating, foraging, other_act, kuks, quaas, moans, flags, twitches, approaches, indifferent, runsfrom, other_int, lat_long):

        squirreltest = self.create(x=x, y=y, unique_squirrel_id=unique_squirrel_id, hectare=hectare, shift=shift,date=date, hectare_sq=hectare_sq,
                age = age, primary_fur = primary_fur, highlight_fur = highlight_fur, combi_fur = combi_fur, color_note = color_note, location = location, above_ground
                = above_ground, spec_loc = spec_loc, running = running, chasing= chasing, climbing = climbing, eating= eating, foraging= foraging, other_act=other_act,kuks = kuks, quaas = quaas, moans=moans, flags=flags, twitches = twitches, approaches = approaches, indifferent = indifferent, runsfrom = runsfrom, other_int = other_int, lat_long = lat_long
                )
        return squirreltest

class SquirrelTest(models.Model):
    x = models.FloatField(
            default = 0,
            )
    y = models.FloatField(
            default = 0,
            )
    unique_squirrel_id = models.CharField(max_length=14,
            default = '',
            )
    hectare = models.CharField(max_length=4,
            default = '',
            )
    AM='AM'
    PM = 'PM'
    shift_choices = [
            (AM, _('AM')),
            (PM, _('PM')),
                ]
    shift = models.CharField(
            max_length = 3,
            choices = shift_choices,
            default = AM,
            )
    date = models.CharField(
            max_length = 9,
            default = '',
            )
    hectare_sq = models.IntegerField(
            default =0,
            )
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHER = ''
    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
        (OTHER, _('')),
    ]
    age = models.CharField(
        blank=True,
        max_length=20,
       # help_text=_("Age"),
        choices=AGE_CHOICES,
        default='',
    )
    primary_fur = models.CharField(
            max_length = 20,
            help_text=_("Primary Fur Color"),
            default='',
             )   
    highlight_fur =models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Highlight Fur Color"),
        default='',
    )
    combi_fur = models.CharField(
        blank=True,
        max_length=40,
        help_text=_("Combine Fur Color"),
        default='',
    )
    color_note = models.CharField(
        blank=True,
        max_length=40,
        help_text=_("Color Note"),
        default='',
    )

    AG = 'Above Ground'
    GP = 'Ground Plane'
    OTHER = ''
    LOCATION_CHOICES = [
       (AG, _('Above Ground')),
        (GP, _('Ground Plane')),
        (OTHER, _('')),
    ]
    location =models.CharField(
        max_length=20,
        help_text=_("Locations"),
        choices=LOCATION_CHOICES,
        default='',
    ) 
    above_ground =models.CharField(
        blank=True,
        max_length=20,
        default='',
        help_text=_("How Far from Ground Please Put The Number. If Found On The Ground Please Put FALSE"),
    )
    spec_loc = models.CharField(
        blank=True,
        max_length=70,
        default='',
        help_text=_("Specific Location"),
    )

    running = models.BooleanField(default=True)
    chasing = models.BooleanField(default=True)
    climbing = models.BooleanField(default=True)
    eating = models.BooleanField(default=True)
    foraging = models.BooleanField(default=True)

    other_act = models.CharField(
        blank=True,
        max_length=30,
        default='',
        help_text=_("Report any other activities and leave it empty if there is none"),
    )
    
    kuks = models.BooleanField(default=True)
    quaas = models.BooleanField(default=True)
    moans = models.BooleanField(default=True)
    flags = models.BooleanField(default=True)
    twitches = models.BooleanField(default=True)
    approaches = models.BooleanField(default=True)
    indifferent = models.BooleanField(default=True)
    runsfrom = models.BooleanField(default=True)
    
    other_int = models.CharField(
        blank=True,
        max_length=30,
        default='',
        help_text=_("Report any other interaction and leave it empty if there is none"),
    )

    lat_long = models.CharField(
        blank=True,
        max_length=30,
        default='',
        )



    objects = SquirrelTestManager()



