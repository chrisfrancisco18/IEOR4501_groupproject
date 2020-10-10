rom django.db import models

class Squirrel(models.Model):
    X=models.FloatField()
    Y=models.FloatField()
    Unique_Squirrel_ID=models.CharField(
            max_length=40)
    Hectare=models.CharField(
            max_length=10)
    Shift=models.CharField(
            max_length=10)
    Date=models.CharField(
            max_length=40)
    Hectare_squirrel_nunber=models.IntegerField()
    Age=models.CharField(
            max_length=20)
    Primary_Fur_Color=models.CharField(
            max_length=20)
    Highlight_Fur_Color=models.CharField(
            max_length=20)
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

# Create your models here

