import asyncio
import time


def myTask(param):
    time.sleep(1)
    return param * 2


coros = [myTask(1) for i in range(10)]

print(coros)
