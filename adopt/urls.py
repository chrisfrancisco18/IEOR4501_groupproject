from django.urls import path, include

from . import views

app_name = 'adopt'

urlpatterns = [
        # path('', views.index),
        path('sightings/', include(extrapatterns)),
]

extra_patterns = [
        path('', views.sightings),
        path('<int:squirrel_id>/', views.detail, name='detail'),
        # path('<slug:squirrel_Unique_Squirrel_ID>/', views.detail, name='detail'),
]
