from exceptions import SessionNotStarted


def validate_session_started(f):
    """
    Decorator that checks _networking.is_connected() returns true
    """
    def wrapped_f(self, *args, **kwargs):
        if self.is_session_started():
            return f(self, *args, **kwargs)
        else:
            raise SessionNotStarted("Command session not started")
    return wrapped_f
