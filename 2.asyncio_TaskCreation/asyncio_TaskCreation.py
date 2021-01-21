import asyncio
import time


async def function1():
    task2 = asyncio.ensure_future(function2())
    time.sleep(3)
    print("function 1()")


async def function2():
    time.sleep(3)
    print("function2()")


event_loop = asyncio.get_event_loop()
task1 = asyncio.ensure_future(function1())
event_loop.run_until_complete(task1)
