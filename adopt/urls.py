from django.urls import path, include

from . import views

app_name = 'adopt'

extra_patterns = [
        path('', views.sightings, name='sightings'),
        # path('<int:squirrel_id>/', views.detail, name='detail'),
        #path('<slug:Unique_Squirrel_ID>/', views.squirrel_detail, name='detail'),
        path('add/', views.add_sighting, name='add'),
]

urlpatterns = [
        # path('', views.index),
        path('map/', views.map),
        path('sightings/', include(extra_patterns)),
]
