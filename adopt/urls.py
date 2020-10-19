from django.urls import path, include

from . import views

app_name = 'adopt'

extra_patterns = [
        path('', views.sightings, name='sightings'),
        # path('<int:squirrel_id>/', views.detail, name='detail'),
        # path for stats
        path('stats/', views.stat_acts),
        path('<str:unique_squirrel_id>/', views.squirrel_detail, name='detail'),
]

urlpatterns = [
        # path('', views.index),
        path('map/', views.map),
        path('sightings/', include(extra_patterns)),
]
