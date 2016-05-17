# -*- coding: utf-8 -*-
import aiohttp

session = aiohttp.ClientSession()


async def geocode(place):
    params = {
        'sensor': 'false',
        'address': place
    }
    async with session.get(
        'https://maps.googleapis.com/maps/api/geocode/json',
        params=params
    ) as response:
        result = await response.json()
        return result['results']
