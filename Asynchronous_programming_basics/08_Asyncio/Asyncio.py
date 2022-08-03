def annie():
    yield "Yes I can"
    yield "Yes I can"
    yield "Yes I can"


def frank():
    yield "No you cant"
    yield "No you cant"
    yield "No you cant"


queue = [annie(), frank()]

print(queue.pop(0))

