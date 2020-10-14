from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Squirrel

# Create your views here.
def index(request):
    return render(request, 'adopt/index.html',{})

# First view /map
# see Squirrel Tracker Doc
"""
def map(request):
    context = {}
    return render(request, 'adopt/map.html', context)
"""

# Second view /sightings
# see Squirrel Tracker Doc
def sightings(request):
    # this will list all squirrel sightings
    squirrels = Squirrel.objects.all()
    
    context = {
       'squirrels':squirrels, 
    }
    
    return render(request, 'adopt/sightings.html', context)
    
# Third view /sightings/<unique-squirrel-id>
# see Squirrel Tracker Doc
def detail(request, Squirrel_ID):
    # this will provide info for particular view (ID)
    squirrel = get_object_or_404(Squirrel, fieldname=Squirrel_ID)
    
    context = {
        'squirrel':squirrel,
    }
    
    return render(request, 'adopt/detail.html', context)

# Fourth view /sightings/add
# see Squirrel Tracker Doc
    
