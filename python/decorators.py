from exceptions import SocketNotInitialized


def is_connected(f):
    """
    Decorator that checks _networking.is_connected() returns true
    """
    def wrapped_f(self, *args, **kwargs):
        if self._networking.is_connected():
            return f(self, *args, **kwargs)
        else:
            raise SocketNotInitialized("Try using wait_for_connection first")
    return wrapped_f