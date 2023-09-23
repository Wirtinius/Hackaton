from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

from asgiref.sync import async_to_sync

from .parser import Parser

parser = Parser()
        
    
class StopsView(APIView):
    @async_to_sync
    async def get(self, request, route_id):
        stops = await parser.get_stops(route_id)
        return Response(stops, status=status.HTTP_200_OK)