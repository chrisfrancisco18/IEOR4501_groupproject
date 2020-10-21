from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse #We could modify this to HttpResponseRedirect
#from .forms import NameForm
from .models import SquirrelTest
from .forms import SquirrelForm

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
    if SquirrelTest.objects.count() > 100:
        sightings = random.sample(list(SquirrelTest.objects.all()), 100)
    else:
        sightings = SquirrelTest.objects.all()
    
    context = {
       'sightings':sightings, 
    }
    
    return render(request, 'adopt/map.html', context)

# Second view /sightings
# see Squirrel Tracker Doc
def sightings(request):
    # this will list all squirrel sightings
    squirrels = SquirrelTest.objects.all()
    
    context = {
       'squirrels': squirrels, 
    }
    
    return render(request, 'adopt/sightings.html', context)
    
# Third view /sightings/<unique-squirrel-id>
# see Squirrel Tracker Doc
def squirrel_detail(request, unique_squirrel_id):
    # this will provide info for particular view (ID)
    # squirrel = get_object_or_404(Squirrel, pk=squirrel_id)
    squirrel = get_object_or_404(SquirrelTest, unique_squirrel_id=unique_squirrel_id)
    form = SquirrelForm(request.POST)
    
    context = {
        'squirrel': squirrel,
        'form': form
    }
    
    return render(request, 'adopt/detail.html', context)

"""
def squirrel_detail(request, uni_sqr_id):
    squirrel = get_object_or_404(SquirrelTest, Unique_Squirrel_ID=uni_sqr_id)
    
    context = {
        'squirrel':squirrel,
    }
    
    return render(request, 'adopt/detail.html', context)
"""

def squirrel_detail_update(request):
    if request.method == 'POST':
        form = NameFormTwo(request.POST)
        # need to recheck this
        # see Lecture 8.16 Forms
        if form.is_valid():
            return form.save()
        else:
            JsonResponse({'errors':form.errors}, status=400)
    else:
        form = NameFormTwo()

    return render(request, 'adopt/add.html', {'form': form})

# Fourth view /sightings/add
def sightings_add(request):
    if request.method == 'GET':
        form = SquirrelForm()
        return render(request, 'adopt/add.html', {'form': form})

    elif request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            squirrel = form.save(commit = False)
            squirrel.save()

            return HttpResponse('Thanks for the adding!')
        else:
            return JsonResponse({'errors':form.errors}, status=400)

    return JsonResponse({}, status=405)


#Fifth view: general stats-> Number of squirrels for each color/Most common actions, colors, etc.
# This one should provide number of squirrels for selected activities
def stat_acts(request):
    squirrels_obj = SquirrelTest.objects
    
    # cannot use get_list_or_404 because it raises an error if the list is empty
    #runnings = get_list_or_404(Squirrel, Running=True)
    #chasings = get_list_or_404(Squirrel, Chasing=True)
    #climbings = get_list_or_404(Squirrel, Climbing=True)
    #eatings = get_list_or_404(Squirrel, Eating=True)
    #foragings = get_list_or_404(Squirrel, Foraging=True)
    
    runnings = squirrels_obj.filter(running=True)
    chasings = squirrels_obj.filter(chasing=True)
    climbings = squirrels_obj.filter(climbing=True)
    eatings = squirrels_obj.filter(eating=True)
    foragings = squirrels_obj.filter(foraging=True)
    
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
    
    # stat_acts_hist(chasings)
    return render(request, 'adopt/stats.html', context)
    
def stat_acts_helper(list_):
    if not list_:
        raise InputError()
    else:
        temp_lat = []
        temp_log = []
        for each in list_:
            temp_lat.append(each.y)
            temp_log.append(each.x)
        return [statistics.mean(temp_lat), statistics.mean(temp_log)]

"""
try to do stat by using matplotlib and pandas
"""
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
        # print(plt.savefig('image.jpg'))

