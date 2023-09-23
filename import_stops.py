import sqlite3
import requests

from core.settings import BUS_LIST


URL = "https://cabinet.transcard.kz/api/v3/bus-route/stops?line-code="


def import_stops():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM map_stop")
    conn.commit()

    id = 0
    bus_codes = []

    for bus in BUS_LIST:
        r = requests.get(URL + str(bus))
        if r.status_code == 200:
            data = r.json()["data"]
            for stop in data["direction_right"]:
                if stop["StopCode"] in bus_codes:
                    continue
                cursor.execute(
                    'INSERT INTO map_stop (id, code, name, lat, long, "order", direction) VALUES (?, ?, ?, ?, ?, ?, ?)',
                    (
                        id,
                        stop["StopCode"],
                        stop["StopDesc"],
                        stop["StopLat"],
                        stop["StopLon"],
                        stop["StopOrder"],
                        1,
                    ),
                )
                id += 1
                bus_codes.append(stop["StopCode"])
            for stop in data["direction_left"]:
                if stop["StopCode"] in bus_codes:
                    continue
                cursor.execute(
                    'INSERT INTO map_stop (id, code, name, lat, long, "order", direction) VALUES (?, ?, ?, ?, ?, ?, ?)',
                    (
                        id,
                        stop["StopCode"],
                        stop["StopDesc"],
                        stop["StopLat"],
                        stop["StopLon"],
                        stop["StopOrder"],
                        0,
                    ),
                )
                id += 1
                bus_codes.append(stop["StopCode"])
            conn.commit()
    conn.close()


if __name__ == "__main__":
    import_stops()
