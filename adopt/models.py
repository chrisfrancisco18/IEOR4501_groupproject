from django.db import models
from django.utils.translation import gettext as _

# Create your models here




class SquirrelManager(models.Manager):
    def create_squirrel(self, x, y, unique_squirrel_id, hectare, shift, date,hectare_sq, age, primary_fur,highlight_fur, combi_fur, color_note, location, above_ground, spec_loc, running, chasing, climbing, eating, foraging, other_act, kuks, quaas, moans, flags, twitches, approaches, indifferent, runsfrom, other_int, lat_long ):
        squirrel = self.create(x=x, y=y, unique_squirrel_id=unique_squirrel_id,hectare=hectare, shift=shift, date=date,hectar_sq=hectare_sq, age=age, primary_fur=primary_fur, highlight_fur=highlight_fur, combi_fur=combi_fur, color_note=color_note, location=location, above_ground=above_ground, spec_loc=spec_loc, running=running, chasing=chasing, climbing=climbing, eating=eating, foraging=foraging, other_act=other_act, kuks=kuks, quaas=quaas, moans=moans, flags=flags, twitches=twitches, approaches=approaches, indifferent=indifferent, runsfrom=runsfrom, other_int=other_int, lat_long=lat_long
)
        return squirrel

class Squirrel(models.Model):
    x = models.FloatField()
    y = models.FloatField()
   # unique_squirrel_id = models.CharField(max_length=14)
    unique_squirrel_id=models.CharField(
        primary_key=True,
        max_length=14,
        help_text=_("The Unique ID"),
    )
    
    hectare=models.CharField(
        blank=True,
        max_length=4,
        help_text=_("Hectare"),
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
            max_length=3)
    

    date=models.DateField(
        help_text=_("Date"),
    )
   # Date=models.CharField(
   #     max_length=9,
   #     help_text=_("Date"),
   # )
    
    hectare_sq=models.IntegerField(
       # blank=True,
        help_text=_("Hectare Number"),
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
       # default=OTHER,
    )
    
    primary_fur_Color=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Primary Fur Color"),
    )
    
    highlight_fur_Color=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Highlight Fur Color"),
    )
    
    combi_fur=models.CharField(
        blank=True,
        max_length=40,
        help_text=_("Combine Fur Color"),
    )
    
    color_note=models.CharField(
        blank=True,
        max_length=40,
        help_text=_("Color Note"),
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
       # default=OTHER,
    )
    
    above_ground=models.CharField(
       # blank=True,
        max_length=20,
        help_text=_("How Far from Ground Please Put The Number. If Found On The Ground Please Put FALSE"),
    )
    
    specific_loc=models.CharField(
       # blank=True,
        help_text=_("Specific Location"),
    )
    
    running=models.BooleanField()
    chasing=models.BooleanField()
    climbing=models.BooleanField()
    eating=models.BooleanField()
    foraging=models.BooleanField()
    
    other_act=models.CharField(
       # blank=True,
        help_text=_("Other Activites"),
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
        help_text=_("Other Interactions"),
    )
    
    lat_long=models.CharField(
        blank=True,
        max_length=100,
    )
    
    def __str__(self):
        return self.Unique_Squirrel_ID


    objects = SquirrelManager()




