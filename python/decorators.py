from exceptions import SocketNotInitialized


def is_connected(f):
    """
    Decorator that checks if self._connection is set
    """
    def wrapped_f(self, *args, **kwargs):
        if self._connection is not None:
            return f(self, *args, **kwargs)
        else:
            raise SocketNotInitialized("Try using wait_for_connection first")
    return wrapped_f