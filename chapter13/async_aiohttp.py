"""
"Asynchronous programming" section example showing how
to use aiohttp to perform asynchronous HTTP calls

"""
import asyncio
# note: local package
from asyncgmaps import geocode, session


PLACES = (
    'Reykjavik', 'Vien', 'Zadar', 'Venice',
    'Wrocław', 'Bolognia', 'Berlin', 'Słubice',
    'New York', 'Dehli',
)


async def fetch_place(place):
    return (await geocode(place))[0]


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

    # aiohttp will raise issue about unclosed
    # ClientSession so we perform cleanup manually
    loop.run_until_complete(session.close())
    loop.close()
