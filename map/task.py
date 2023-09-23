import aiohttp
from .parser import get_stops
from asgiref.sync import async_to_sync

@async_to_sync
async def find(first_bus_number, last_bus_number):
    for i in range(first_bus_number, last_bus_number):
        stops_data = await get_stops(route_id=i)
        if stops_data is not None:
            print(i)

