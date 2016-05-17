"""
"Asynchronous programming" section example showing
how to employ `futures` and threading/multiprocessing
to use non-async libraries in asyncio-based applications

"""
import asyncio
from gmaps import Geocoding

api = Geocoding()



PLACES = (
    'Reykjavik', 'Vien', 'Zadar', 'Venice',
    'Wrocław', 'Bolognia', 'Berlin', 'Słubice',
    'New York', 'Dehli',
)


async def fetch_place(place):
    coro = loop.run_in_executor(None, api.geocode, place)
    result = await coro
    return result[0]


async def present_result(result):
    geocoded = await result
    print("{:>25s}, {:6.2f}, {:6.2f}".format(
        geocoded['formatted_address'],
        geocoded['geometry']['location']['lat'],
        geocoded['geometry']['location']['lng'],
    ))


async def main():
    await asyncio.wait([
        present_result(fetch_place(place))
        for place in PLACES
    ])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    loop.close()
