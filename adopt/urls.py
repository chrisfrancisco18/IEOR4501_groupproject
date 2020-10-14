from django.urls import path

from . import views

app_name = 'adopt'

urlpatterns = [
        #path('', views.index),
        path('sightings/', views.sightings),
        path('<int:squirrel_id>/', views.detail, name='detail'),
        ]
