import json
import aiohttp


class Parser:
    MAIN_URL = "https://cabinet.transcard.kz/api/v3/bus-route"

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
        28,
        29,
        31,
        32,
        34,
        35,
        36,
        37,
        39,
        40,
        41,
        44,
        46,
        47,
        48,
        50,
        51,
        52,
        53,
        54,
        56,
        60,
        61,
        64,
        70,
        71,
        72,
        73,
        80,
        81,
        120,
    ]

    async def get_stops(self, route_id: int):
        url = self.MAIN_URL + "/stops" + f"?line-code={route_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                result = await response.json()
        return result["data"]
