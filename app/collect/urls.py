from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('geo_location', views.geo_location, name='geo_location'),
]