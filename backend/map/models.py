from django.db import models


class Stop(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    order = models.IntegerField(null=True)
    direction = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Bus(models.Model):
    bus_number = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    ts_code = models.CharField(max_length=10)
    direction = models.BooleanField(default=False)

    stop = models.ForeignKey(Stop, on_delete=models.CASCADE, null=True, to_field="code")

    def __str__(self):
        return f"{self.bus_number} - {self.ts_code}"


class Route(models.Model):
    bus_number = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    direction = models.BooleanField(default=False)
