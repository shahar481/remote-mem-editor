from abc import ABC


class BaseMessage(ABC):
    """
    Abstract class which all message types inherit from
    """

    def __init__(self, message_type, message):
        self.message_type = message_type
        self.message = bytes(message)
