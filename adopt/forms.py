from django.forms import ModelForm

from .models import Squirrel

class NameForm(ModelForm):
  class Meta:
    model = Squirrel
    fields = [
      # update this later
      # See the document
      'Latitude',
      'Longitude',
      'Unique_Squirrel_ID',
      'Shift',
      'Date',
      'Age',
      ]
