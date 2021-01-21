import asyncio
import time


async def waiter():
    task1 = asyncio.ensure_future(cook('pasta', 5))
    task2 = asyncio.ensure_future(cook('lobster', 20))
    task3 = asyncio.ensure_future(cook('salad', 2))
    print(task1)
    print(task2)
    print(task3)
    await asyncio.wait([task1, task2, task3])

    # print("Waiter: All dishes cooked")


async def cook(order: str, cook_time: int):
    print(f"Getting {order} order")
    await asyncio.sleep(cook_time)
    print(order, " ready")


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.ensure_future(waiter()))
event_loop.close()

