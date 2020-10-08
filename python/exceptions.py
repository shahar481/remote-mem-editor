class SocketNotInitialized(Exception):
    pass


class ErrorMessageReceived(Exception):
    pass


class InvalidParameters(Exception):
    pass


class UnexpectedMessageType(Exception):
    pass


class SessionNotStarted(Exception):
    pass


class CommandTypesDontMatch(Exception):
    pass
