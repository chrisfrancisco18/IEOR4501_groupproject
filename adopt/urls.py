from django.urls import path

from . import views

app_name = 'adopt'

urlpatterns = [
        # path('', views.index),
        path('sightings/', include(extrapatterns)),
]

extrapatterns = [
        path('', views.sightings),
        path('<int:squirrel_id>/', views.detail, name='detail'),
        # path('<slug:squirrel_Unique_Squirrel_ID>/', views.detail, name='detail'),
]
