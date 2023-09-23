import json
import aiohttp



MAIN_URL = "https://cabinet.transcard.kz/api/v3/bus-route"

BUS_LIST = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 35, 36, 37, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 59, 60, 61, 64, 69, 70, 71, 72, 73, 80, 81, 120, 300, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 326
]


async def get_stops(route_id: int):
    url = MAIN_URL + "/stops" + f"?line-code={route_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
    if result.get("data")["direction_right"] or result.get("data")["direction_left"]:
        return result["data"]
    else:
        return None