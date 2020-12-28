import collections
import contextvars

from .task import Task


# 事件对象
class Handle:
    def __init__(self, callback, loop, context=None):
        context = contextvars.copy_context()
        self._context = context
        self._loop = loop
        self._callback = callback

    def run(self):
        self._callback()


class EventLoop:
    def __init__(self):
        self.stopping = False
        self.loop_funcs = collections.deque()

        # 事件队列
        self._ready = collections.deque()

    def create_task(self, coro):
        return Task(coro)

    def call_soon(self, callback, context):
        # 将事件添加到队列里
        handle = Handle(callback, self, context)
        self._ready.append(handle)
        return handle

    def run_once(self):
        # 执行队列里的事件
        ntodo = len(self._ready)
        for i in range(ntodo):
            handle = self._ready.popleft()
            if handle._cancelled:
                continue
            handle.run()

    def run_forever(self):
        while True:
            self.run_once()
            if self.stopping:
                break


def get_running_loop() -> object:
    # do_something
    current_loop = False
    # 获取到当前线程中运行的loop
    if current_loop:
        return current_loop
    else:
        new_loop = EventLoop()
        return new_loop


def new_event_loop():
    return EventLoop()


def get_event_loop():
    loop = get_running_loop()

    if not loop:
        loop = new_event_loop()

    return loop