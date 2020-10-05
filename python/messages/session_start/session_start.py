import struct

from messages.base import BaseMessage

MESSAGE_TYPE = 1
SESSION_MESSAGE_FORMAT = "!{0}"


class SessionStartMessage(BaseMessage):
    def __init__(self, message):
        """
        Class for session start messages from the client
        :param message: Cut message, without the length parameter or the message type byte
        """
        super().__init__(MESSAGE_TYPE, message)

    @property
    def supported_commands(self):
        return struct.unpack(SESSION_MESSAGE_FORMAT.format("B"*len(self.message)), self.message)
