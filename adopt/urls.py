from django.urls import path

from . import views

# Should we change the name?
app_name = 'adopt'

urlpatterns = [
        #path('', views.index),
        path('', views.sightings),
        ]
