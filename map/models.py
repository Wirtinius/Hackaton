from django.db import models

class Stop(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    order = models.IntegerField()
    direction = models.BooleanField()


class Bus(models.Model):
    bus_number = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()