import asyncio
import time


async def waiter():
    await cook('pasta', 5)
    await cook('lobster', 10)
    await cook('salad', 2)

    print("Waiter: All dishes cooked")


async def cook(order: str, cook_time: int):
    print(f"Getting {order} order")
    time.sleep(cook_time)
    print(order, " ready")


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.ensure_future(waiter()))
