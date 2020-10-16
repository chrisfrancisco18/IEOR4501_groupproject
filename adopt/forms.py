from django import forms
from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext as _
from .models import Squirrel

class SquirrelForm(ModelForm):
    #your_name = forms.CharField(label='Your name', max_length=100)

    sq_lat = forms.FloatField(label='Latitude')
    sq_longi = forms.FloatField(label='Longitude')
    sq_id = forms.SlugField(label='Unique ID', max_length =14)
    AM = "AM"
    PM = "PM"
    SHIFT_CHOICES = [
        (AM, _('AM')),
        (PM, _('PM')),
        ]
        
    sq_shift =forms.CharField(max_length=3, choices= SHIFT_CHOICES, default=AM)
    sq_date = forms.DateField(auto_now=False, auto_now_add=False)
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHER = ''
    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
        (OTHER, _('')),
    ]
    sq_age = forms.CharField(
            blank=True,
            max_length=20,
            choices=AGE_CHOICES,
            default=OTHER,
            )
