import asyncio


async def func1():
    while True:
        print("Function test1 Start")
        await asyncio.sleep(2)
        print("Function test1 End")


async def func2():
    while True:
        print("Function2 Start")
        await asyncio.sleep(1)
        print("Function2 End")


async def controller():
    t1 = asyncio.ensure_future(func1())
    t2 = asyncio.ensure_future(func2())

    print(t1)
    print(t2)
    #await asyncio.gather(t1, t2)


loop = asyncio.get_event_loop()
loop.run_until_complete(controller())
loop.close()

