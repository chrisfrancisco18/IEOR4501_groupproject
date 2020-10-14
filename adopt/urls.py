from django.urls import path, include

from . import views

app_name = 'adopt'

extra_patterns = [
        path('', views.sightings),
        path('<int:squirrel_id>/', views.detail, name='detail'),
        # path('<slug:squirrel_Unique_Squirrel_ID>/', views.detail, name='detail'),
]

urlpatterns = [
        # path('', views.index),
        path('sightings/', include(extra_patterns)),
]
