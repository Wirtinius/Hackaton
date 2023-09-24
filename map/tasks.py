import json

import requests
from celery import shared_task
from core.settings import BUS_LIST

from .models import Bus, Stop


URL = "https://cabinet.transcard.kz/api/v3/bus-route/busses?line-code="


def convert_stop_code_to_string(stop_code: str):
    return "0" * (5 - len(stop_code)) + stop_code


@shared_task
def update_bus_locations():
    total_count = 0
    total_stops = 0

    for bus_number in BUS_LIST:
        r = requests.get(URL + str(bus_number))
        if r.status_code == 200:
            data = r.json()["data"]
            for bus in data:
                if bus["Direction"] is None:
                    continue

                stop_code = convert_stop_code_to_string(bus["StopCode"])

                stop, created = Stop.objects.get_or_create(code=stop_code)

                if created:
                    total_stops += 1
                    stop.delete()
                    continue

                Bus.objects.update_or_create(
                    ts_code=bus["TSCode"],
                    defaults={
                        "lat": bus["Latitude"],
                        "long": bus["Longitude"],
                        "ts_code": bus["TSCode"],
                        "direction": bus["Direction"],
                        "bus_number": bus_number,
                        "stop": stop,
                    },
                )
                total_count += 1
    return f"Updated {total_count} buses and {total_stops} stops"
