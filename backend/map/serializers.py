from rest_framework import serializers

from .models import Stop, Route, Bus


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    stop = StopSerializer()

    class Meta:
        model = Bus
        fields = "__all__"
