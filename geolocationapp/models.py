from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GeolocationInformation (models.Model):
    geodescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.geodescription

    class Meta():
        db_table='geodescription'
        verbose_name_plural='geodescriptions'

class GeolocationData(models.Model):
    geoname=models.CharField(max_length=255)
    latdegree=models.IntegerField(blank=True, null=True)
    latminute=models.IntegerField(blank=True, null=True)
    latsecond=models.FloatField(blank=True, null=True)
    latdirection=models.CharField(max_length=1, blank=True, null=True)
    longdegree=models.IntegerField(blank=True, null=True)
    longminute=models.IntegerField(blank=True, null=True)
    longsecond=models.FloatField(blank=True, null=True)
    longdirection=models.CharField(max_length=1, blank=True, null=True)
    latitude=models.FloatField(blank=True, null=True)
    longitude=models.FloatField(blank=True, null=True)
    altitude=models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.geoname

    class Meta():
        db_table='geolocationdata'
        verbose_name_plural='geolocationdatas'
