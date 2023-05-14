from django.contrib import admin
from django.urls import path
from .views import addpoint, viewpoints, allpoints

urlpatterns = [
    path('', addpoint, name='index'),
    path('viewpoints', viewpoints, name='viewpoints'),
    path('allpoints', allpoints, name='allpoints'),
]
