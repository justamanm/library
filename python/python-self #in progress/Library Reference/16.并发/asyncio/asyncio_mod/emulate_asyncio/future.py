import contextvars


class Future:
    _state = "_PENDING"     # 默认是_PENDING
    _result = None
    _exception = None

    def __init__(self, coro):
        pass

    def add_done_callback(self):
        context = contextvars.copy_context()
        self._callbacks.append((fn, context))

    def done(self):
        return self._state != "_PENDING"

