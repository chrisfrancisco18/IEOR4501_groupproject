from django.shortcuts import render, get_object_or_404, get_list_or_404
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
def squirrel_detail(request, uni_sqr_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=uni_sqr_id)
    
    context = {
        'squirrel':squirrel,
    }
    
    return render(request, 'adopt/detail.html', context)

def squirrel_detail_update(request):
    if request.method == 'POST':
        form = NameFormTwo(request.POST)
        # need to recheck this
        # see Lecture 8.16 Forms
        if form.is_valid():
            return form.save()
        else:
            JsonResponse{{'errors':form.errors}, status = 400}
    else:
        form = NameFormTwo()

    return render(request, 'add.html', {'form': form})
"""

# Fourth view /sightings/add
# see Squirrel Tracker Doc
"""
def add_sighting(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('//')

    else:
        form = NameForm()

    return render(request, 'add.html', {'form': form})    #need to check this line

"""

#Fifth view: general stats-> Number of squirrels for each color/Most common actions, colors, etc.
# This one should provide number of squirrels for selected activities
def stat_acts(request):
    squirrels_obj = Squirrel.objects
    
    # cannot use get_list_or_404 because it raises an error if the list is empty
    #runnings = get_list_or_404(Squirrel, Running=True)
    #chasings = get_list_or_404(Squirrel, Chasing=True)
    #climbings = get_list_or_404(Squirrel, Climbing=True)
    #eatings = get_list_or_404(Squirrel, Eating=True)
    #foragings = get_list_or_404(Squirrel, Foraging=True)
    
    runnings = squirrels_obj.filter(Running=True)
    chasings = squirrels_obj.filter(Chasing=True)
    climbings = squirrels_obj.filter(Climbing=True)
    eatings = squirrels_obj.filter(Eating=True)
    foragings = squirrels_obj.filter(Foraging=True)
    
    print(type(runnings))
    
    if running:
        for running in runnings:
            print(running)
    
    context = {
        'runnings':runnings,
        'chasings':chasings,
        'climbings':climbings,
        'eatings':eatings,
        'foragings':foragings,
    }
    
    print(context)
    return render(request, 'adopt/stats.html', context)
    
