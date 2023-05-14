from django.contrib.gis.admin import OSMGeoAdmin
from .models import Points
from django.contrib.gis import admin


@admin.register(Points)
class PointsAdmin(OSMGeoAdmin):
    list_display = ('name', 'description', 'location')
