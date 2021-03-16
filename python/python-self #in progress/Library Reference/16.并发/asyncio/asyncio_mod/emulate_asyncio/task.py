import contextvars
from emulate_asyncio.events import get_event_loop, EventLoop
from .future import Future


class Task(Future):
    def __init__(self, coro):
        super().__init__(coro)
        self._state = "_PENDING"    # _CANCELLED _FINISHED
        self._callbacks = []
        self.loop: EventLoop = get_event_loop()

        self._coro = coro
        self._context = contextvars.copy_context()

        self.loop.call_soon(self.step, context=self._context)
        _register_task(self)    # TODO

    def step(self):
        result = self._coro.send(None)

    def __wakeup(self, future):
        future.result()
        self.step()
        self = None     # 删除task

