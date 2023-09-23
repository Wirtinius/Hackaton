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
        routes = Route.objects.filter(bus_number=bus_number)
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)
