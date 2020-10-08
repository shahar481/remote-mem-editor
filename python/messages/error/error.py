from messages.base import BaseMessage
from exceptions import ErrorMessageReceived

MESSAGE_TYPE = 2


class ErrorMessage(BaseMessage):
    def __init__(self, message=""):
        """
        Class for incoming error messages from the client
        :param message: Cut message, without the length parameter or the message type byte
        """
        super().__init__(MESSAGE_TYPE, message)
        if len(message) != 0:
            raise ErrorMessageReceived(message)

