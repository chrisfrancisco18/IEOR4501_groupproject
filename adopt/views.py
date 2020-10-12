from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Squirrel

# Create your views here.
def index(request):
    return render(request, 'adopt/index.html',{})

# First view 
# see Squirrel Tracker Doc
"""
def map(request):
    context = {}
    return render(request, 'adopt/map.html', context)
"""

# Second view
# see Squirrel Tracker Doc
def sightings(request, squirrel.id):
    squirrel = get_object_or_404(Squirrel, pk=squirrel.id)
    
    context = {
       'squirrel':squirrel, 
    }
    
    return render(request, 'adopt/sightings.html', context)
    
