import asyncio


async def worker():
    print("Hello from worker")

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*[worker() for i in range(5)]))
    loop.close()

except KeyboardInterrupt:
    pass

finally:
    loop.close()