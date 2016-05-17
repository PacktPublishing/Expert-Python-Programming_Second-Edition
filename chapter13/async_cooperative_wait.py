"""
"Asynchronous programming" section example showing how
two coroutines cooperate by releasing control to event
loop on blocking calls.

"""
import random
import asyncio


async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print(
            "{} waited {} seconds"
            "".format(name, time_to_sleep)
        )


async def main():
    await asyncio.wait([waiter("foo"), waiter("bar")])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
