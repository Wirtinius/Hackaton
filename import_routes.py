import sqlite3
import requests

from core.settings import BUS_LIST


URL = "https://cabinet.transcard.kz/api/v3/bus-route/actual-routes?line-code="


def import_routes():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM map_route")
    conn.commit()

    id = 0

    for bus in BUS_LIST:
        r = requests.get(URL + str(bus))
        if r.status_code == 200:
            data = r.json()["data"]
            for route in data["direction_right"][0]:
                cursor.execute(
                    "INSERT INTO map_route (id, bus_number, lat, long, direction) VALUES (?, ?, ?, ?, ?)",
                    (
                        id,
                        bus,
                        route["Lat"],
                        route["Lon"],
                        1,
                    ),
                )
                id += 1
            for route in data["direction_left"][0]:
                cursor.execute(
                    "INSERT INTO map_route (id, bus_number, lat, long, direction) VALUES (?, ?, ?, ?, ?)",
                    (
                        id,
                        bus,
                        route["Lat"],
                        route["Lon"],
                        0,
                    ),
                )
                id += 1
            conn.commit()
    conn.close()


if __name__ == "__main__":
    import_routes()
