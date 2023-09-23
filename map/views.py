from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from asgiref.sync import async_to_sync

from .models import Stop, Route
from .serializers import StopSerializer, RouteSerializer


class StopsView(APIView):
    def get(self, request):
        stops = Stop.objects.all()
        serializer = StopSerializer(stops, many=True)
        return Response(serializer.data)


class RoutesView(APIView):
    def get(self, request, bus_number):
        direction_true_routes = Route.objects.filter(
            bus_number=bus_number, direction=True
        )
        direction_false_routes = Route.objects.filter(
            bus_number=bus_number, direction=False
        )

        direction_true_serializer = RouteSerializer(direction_true_routes, many=True)
        direction_false_serializer = RouteSerializer(direction_false_routes, many=True)

        response = {
            "direction_true": direction_true_serializer.data,
            "direction_false": direction_false_serializer.data,
        }

        return Response(response)
