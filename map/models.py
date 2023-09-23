from django.db import models


class Stop(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    order = models.IntegerField()
    direction = models.BooleanField(default=False)


class Bus(models.Model):
    bus_number = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    ts_code = models.CharField(max_length=10)
    direction = models.BooleanField(default=False)

    stop = models.ForeignKey(Stop, on_delete=models.CASCADE, null=True, to_field="code")


class Route(models.Model):
    bus_number = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    direction = models.BooleanField(default=False)
