from emulate_asyncio.events import get_event_loop
from emulate_asyncio.future import Future


def run(coro):
    loop = get_event_loop()
    future = loop.create_task(coro)

    loop.run_forever()















