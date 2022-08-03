import asyncio

async def f2():
    print("Start f2()")
    await asyncio.sleep(2)
    print("Stop f2()")
async def f1():
    print("Start f1()")
    await  f2()
    print("Stop f1()")


task = asyncio.ensure_future(f1())
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
loop.close()
print("Loop closed")

