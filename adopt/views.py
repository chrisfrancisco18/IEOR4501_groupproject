from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse #We could modify this to HttpResponseRedirect
#from .forms import NameForm

from .models import Squirrel
import random

# Create your views here.
def index(request):
    return render(request, 'adopt/index.html',{})

# First view /map
# see Squirrel Tracker Doc
def map(request):
    # we only plot 100 sightings
    # we'll randomly select 100 sightings unless there are less than a hundred
    if Squirrel.objects.count() > 100:
        sightings = random.sample(Squirrel.objects.all(), 100)
    else:
        sightings = Squirrel.objects.all()
    
    print(sightings)
    context = {
       'sightings':sightings, 
    }
    
    return render(request, 'adopt/map.html', context)

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
def squirrel_detail(request, Unique_Squirrel_ID):
    # this will provide info for particular view (ID)
    # squirrel = get_object_or_404(Squirrel, pk=squirrel_id)
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)
    
    context = {
        'squirrel':squirrel,
    }
    
    return render(request, 'adopt/detail.html', context)

"""
def detail(request, uni_sqr_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID__exact=uni_sqr_id)
    
    context = {
        'squirrel':squirrel,
    }
    
    return render(request, 'adopt/detail.html', context)
"""

# Fourth view /sightings/add
# see Squirrel Tracker Doc
def add_sighting(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            return HttpResponse('/Thanks for the adding!/')
    else:
        form = SquirrelForm()
    return render(request, 'adopt/add.html', {'form': form})    #need to check this line


#Fifth view: general stats-> Number of squirrels for each color/Most common actions, colors, etc.
"""
"""
