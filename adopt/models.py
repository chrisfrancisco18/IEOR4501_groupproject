from django.db import models
from django.utils.translation import gettext as _

# Create your models here

class Squirrel(models.Model):
    X=models.FloatField(
        help_text=_("Latitude"),
    )
    Y=models.FloatField(
        help_text=_("Longitude"),
    )
    Unique_Squirrel_ID=models.CharField(
        max_length=14,
        help_text=_("The Unique ID of Squirrel Sighting"),
    )
    Hectare=models.CharField(
        max_length=4,
    )
    
    # Only two choice for Shift
    AM = 'AM'
    PM = 'PM'
    
    SHIFT_CHOICES = [
        (AM, _('AM')),
        (PM, _('PM')),
    ]
    
    Shift=models.CharField(
        max_length=3,
        choices=SHIFT_CHOICES,
        default=AM,
    )
    
    Date=models.CharField(
        max_length=9
        help_text=_("Date"),
    )
    
    Hectare_squirrel_nunber=models.IntegerField(
        help_text=_("Hectare Number"),
    )
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHER = ''
    
    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
        (OTHER, _('')),
    ]
    
    Age=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Sex"),
        choices=AGE_CHOICES,
        default=OTHER,
    )
    
    Primary_Fur_Color=models.CharField(
        blank=True,
        max_length=20
        help_text=_("Primary Fur Color"),
    )
    
    Highlight_Fur_Color=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Highlight Fur Color"),
    )
    
    Combi_Fur_Color=models.CharField(
            max_length=40)
    Color_Notes=models.CharField(
            max_length=100)
    Location=models.CharField(
            max_length=20)
    Above_Ground=models.CharField(
            max_length=20)
    Specific_Location=models.CharField(
            max_length=100)
    Running=models.BooleanField()
    Chasing=models.BooleanField()
    Climbing=models.BooleanField()
    Eating=models.BooleanField()
    Foraging=models.BooleanField()
    Other_Activ=models.CharField(
            max_length=100)
    Kuks=models.BooleanField()
    Quaas=models.BooleanField()
    Moans=models.BooleanField()
    Tail_flags=models.BooleanField()
    Tail_twitch=models.BooleanField()
    Approaches=models.BooleanField()
    Indifferent=models.BooleanField()
    Runs_from=models.BooleanField()
    Other_Inter=models.CharField(
            max_length=100)
    Lat_Long=models.CharField(
            max_length=100)
    
    def __str__(self):
        return self.Unique_Squirrel_ID
