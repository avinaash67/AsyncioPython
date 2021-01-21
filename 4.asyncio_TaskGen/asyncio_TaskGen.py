import asyncio
import  time


async def worker1():
    time.sleep(1)
    print("I am worker1")


async def taskgeneratorfunc():
    pending = asyncio.Task.all_tasks()
    print(pending)
    for i in range(5):
        asyncio.ensure_future(worker1())


loop = asyncio.get_event_loop()
loop.run_until_complete(taskgeneratorfunc())
loop.close()