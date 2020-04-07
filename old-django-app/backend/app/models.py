from django.conf import settings
from django.db import models


class SkiArea(models.Model):
    name = models.CharField(max_length=256)
    cur_temp = models.IntegerField(max_length=5)
    cur_depth = models.IntegerField(max_length=5)
    ytd = models.IntegerField(max_length=5)
    wind_dir = models.CharField(max_length=256)
    wind_speed = models.IntegerField(max_length=5)
    new_snow_12 = models.IntegerField(max_length=5)
    new_snow_24 = models.IntegerField(max_length=5)
    new_snow_48 = models.IntegerField(max_length=5)


    def __str__(self):
        return self.name