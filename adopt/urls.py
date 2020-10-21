from django.urls import path, include

from . import views

app_name = 'adopt'

extra_patterns = [
        path('', views.sightings, name='sightings'),
        path('add/', views.sightings_add, name='sightings_add'),
        path('stats/', views.stat_acts),
        path('test/',views.stat_acts_hist, name='test'),
        path('<str:unique_squirrel_id>/', views.squirrel_detail, name='detail'),
]

urlpatterns = [
        path('map/', views.map),
        path('sightings/', include(extra_patterns)),
]

