"""
"Multiprocessing" section example showing how
to `multiprocessing.dummy` can be used as an
abstraction layer over threads.

"""
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool

from gmaps import Geocoding

api = Geocoding()


PLACES = (
    'Reykjavik', 'Vien', 'Zadar', 'Venice',
    'Wrocław', 'Bolognia', 'Berlin', 'Słubice',
    'New York', 'Dehli',
)

POOL_SIZE = 4


def fetch_place(place):
    return api.geocode(place)[0]


def present_result(geocoded):
    print("{:>25s}, {:6.2f}, {:6.2f}".format(
        geocoded['formatted_address'],
        geocoded['geometry']['location']['lat'],
        geocoded['geometry']['location']['lng'],
    ))


def main(use_threads=False):
    if use_threads:
        pool_cls = ThreadPool
    else:
        pool_cls = ProcessPool

    with pool_cls(POOL_SIZE) as pool:
        results = pool.map(fetch_place, PLACES)

    for result in results:
        present_result(result)


if __name__ == "__main__":
    main()
