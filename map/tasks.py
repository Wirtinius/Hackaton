import json

import requests
from celery import shared_task
from core.settings import BUS_LIST

from .models import Bus


URL = "https://cabinet.transcard.kz/api/v3/bus-route/busses?line-code="


@shared_task
def update_bus_locations():
    for bus_number in BUS_LIST:
        r = requests.get(URL + str(bus_number))
        if r.status_code == 200:
            data = r.json()["data"]
            for bus in data:
                if bus["Position"] == 0:
                    continue
                Bus.objects.update_or_create(
                    ts_code=bus["TSCode"],
                    defaults={
                        "lat": bus["Latitude"],
                        "long": bus["Longitude"],
                        "ts_code": bus["TSCode"],
                        "direction": bus["Direction"],
                        "bus_number": bus_number,
                        "stop": bus["StopCode"],
                    },
                )
    return True
