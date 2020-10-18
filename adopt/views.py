from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse #We could modify this to HttpResponseRedirect
#from .forms import NameForm
from .models import Squirrel

# for /map
import random
# for /stats
import statistics

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
    
    # print(type(runnings))
    
    found_run = False
    run_avg_lat = 0.0
    run_avg_log = 0.0
    if runnings:
        found_run = True
        run_avg_lat, run_avg_log = stat_acts_helper(runnings)
        
    found_chase = False
    chase_avg_lat = 0.0
    chase_avg_log = 0.0
    if chasings:
        found_chase = True
        chase_avg_lat, chase_avg_log = stat_acts_helper(chasings)
        
    found_climb = False
    climb_avg_lat = 0.0
    climb_avg_log = 0.0
    if climbings:
        found_climb = True
        climb_avg_lat, climb_avg_log = stat_acts_helper(climbings)
    
    found_eat = False
    eat_avg_lat = 0.0
    eat_avg_log = 0.0
    if eatings:
        found_eat = True
        eat_avg_lat, eat_avg_log = stat_acts_helper(eatings)
        
    found_forage = False
    forage_avg_lat = 0.0
    forage_avg_log = 0.0
    if foragings:
        found_forage = True
        forage_avg_lat, forage_avg_log = stat_acts_helper(foragings)
        
    context = {
        'runnings':runnings,
        'found_run':found_run,
        'run_avg_lat':run_avg_lat,
        'run_avg_log':run_avg_log,
        'chasings':chasings,
        'found_chase':found_chase,
        'chase_avg_lat':chase_avg_lat,
        'chase_avg_log':chase_avg_log,
        'climbings':climbings,
        'found_climb':found_climb,
        'climb_avg_lat':climb_avg_lat,
        'climb_avg_log':climb_avg_log,
        'eatings':eatings,
        'found_eat':found_eat,
        'eat_avg_lat':eat_avg_lat,
        'eat_avg_log':eat_avg_log,
        'foragings':foragings,
        'found_forage':found_forage,
        'forage_avg_lat':forage_avg_lat,
        'forage_avg_log':forage_avg_log,
    }
    
    stat_acts_hist(chasings)
    return render(request, 'adopt/stats.html', context)
    
def stat_acts_helper(list_):
    if not list_:
        raise InputError()
    else:
        temp_lat = []
        temp_log = []
        for each in list_:
            temp_lat.append(each.Latitude)
            temp_log.append(each.Longitude)
        return [statistics.mean(temp_lat), statistics.mean(temp_log)]

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def stat_acts_hist(list_):
    if not list_:
        raise InputError()
    else:
        temp_lat = []
        temp_log = []
        for each in list_:
            temp_lat.append(each.Latitude)
            temp_log.append(each.Longitude)
        # temp_list = list(range(len(list_)))
        # print(temp_list)
        dataset = pd.DataFrame(np.transpose(np.array([temp_lat, temp_log])),columns=['Latitude', 'Longitude'])
        print(dataset.describe())
        fig = dataset.hist()
        plt.show()
        plt.savefig('image.jpg')
