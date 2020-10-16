from django.forms import ModelForm

from .models import Squirrel

class NameForm(ModelForm):
  class Meta:
    model = Squirrel
    fields = [
      # update this later
      'Latitude',
      'Longitude',
      ]
