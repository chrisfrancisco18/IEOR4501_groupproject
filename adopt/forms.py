from django import forms
from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext as _

from .models import SquirrelTest

class SquirrelForm(ModelForm):
    class Meta:
        model = SquirrelTest
        fields = ['x', 'y', 'unique_squirrel_id', 'shift', 'date', 'age']
