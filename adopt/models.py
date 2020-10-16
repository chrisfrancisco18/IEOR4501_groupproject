from django.db import models
from django.utils.translation import gettext as _

# Create your models here

class Squirrel(models.Model):
    # I messed up the coordinate X is longitude and Y is latitide
    # This code has not been fixed yet
    Latitude=models.FloatField(help_text=_("Latitude"))
    Longitude=models.FloatField(help_text=_("Longitude"))
    
    """
    Unique_Squirrel_ID=models.CharField(
        max_length=14,
        help_text=_("The Unique ID"),
    ) 
    """
    
    # use Unique Squirrel ID as a primary key
    Unique_Squirrel_ID=models.SlugField(
        primary_key=True,
        max_length=14,
        help_text=_("The Unique ID"),
    )
    
    Hectare=models.CharField(
        blank=True,
        max_length=4,
        help_text=_("Hectare"),
    )
    
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
    
    """
    Date=models.DateField(
        help_text=_("Date"),
    )
    """
    Date=models.CharField(
        max_length=9,
        help_text=_("Date"),
    )
    
    Hectare_squirrel_nunber=models.IntegerField(
        blank=True,
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
        help_text=_("Age"),
        choices=AGE_CHOICES,
        default=OTHER,
    )
    
    Primary_Fur_Color=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Primary Fur Color"),
    )
    
    Highlight_Fur_Color=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Highlight Fur Color"),
    )
    
    Combi_Fur_Color=models.CharField(
        blank=True,
        max_length=40,
        help_text=_("Combine Fur Color"),
    )
    
    Color_Notes=models.CharField(
        blank=True,
        max_length=40,
        help_text=_("Color Note"),
    )
    
    AG = 'Above Ground'
    GP = 'Ground Plane'
    OTHER = ''
    
    LOCATION_CHOICES = [
        (AG, _('Above Ground')),
        (GP, _('Ground Plane')),
        (OTHER, _('')),
    ]
    
    Location=models.CharField(
        max_length=20,
        help_text=_("Locations"),
        choices=LOCATION_CHOICES,
        default=OTHER,
    )
    
    Above_Ground=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("How Far from Ground Please Put The Number. If Found On The Ground Please Put FALSE"),
    )
    
    Specific_Location=models.TextField(
        blank=True,
        help_text=_("Specific Location"),
    )
    
    Running=models.BooleanField()
    Chasing=models.BooleanField()
    Climbing=models.BooleanField()
    Eating=models.BooleanField()
    Foraging=models.BooleanField()
    
    Other_Activ=models.TextField(
        blank=True,
        help_text=_("Other Activites"),
    )
    
    Kuks=models.BooleanField()
    Quaas=models.BooleanField()
    Moans=models.BooleanField()
    Tail_flags=models.BooleanField()
    Tail_twitch=models.BooleanField()
    Approaches=models.BooleanField()
    Indifferent=models.BooleanField()
    Runs_from=models.BooleanField()
    
    Other_Inter=models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Other Interactions"),
    )
    
    Lat_Long=models.CharField(
        blank=True,
        max_length=100,
    )
    
    def __str__(self):
        return self.Unique_Squirrel_ID
