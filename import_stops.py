import sqlite3
import requests


URL = "https://cabinet.transcard.kz/api/v3/bus-route/stops?line-code="

BUS_LIST = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    28,
    29,
    30,
    31,
    32,
    33,
    35,
    36,
    37,
    39,
    40,
    41,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    56,
    57,
    59,
    60,
    61,
    64,
    69,
    70,
    71,
    72,
    73,
    80,
    81,
    120,
    300,
    302,
    303,
    304,
    305,
    306,
    307,
    308,
    309,
    310,
    311,
    312,
    313,
    314,
    315,
    316,
    317,
    318,
    319,
    320,
    321,
    322,
    323,
    326,
]


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
