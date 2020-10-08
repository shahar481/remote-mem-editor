import struct


from exceptions import InvalidParameters, CommandTypesDontMatch
from messages.base import BaseMessage


MESSAGE_TYPE = 4
COMMAND_TYPE_LOCATION = 0


class CommandDataMessage(BaseMessage):
    def __init__(self, message=None, command_type=None, command_data=None):
        """
        Class for in/out facing command data messages, set either message or both command_type and command_data
        :param message: Full message, unparsed, with command type and command data inside it
        :param command_type: Only set if message is not set, Command type in num
        :param command_data: Only set if message is not set, Data of command
        """
        if message is None and (command_type is None or command_data is None):
            raise InvalidParameters()
        if command_type is not None and command_data is not None:
            if isinstance(command_data, str):
                command_data = command_data.encode()
            message = struct.pack("B", command_type) + command_data
        super().__init__(MESSAGE_TYPE, message)

    @property
    def command_type(self):
        return self.message[COMMAND_TYPE_LOCATION]

    @property
    def command_data(self):
        return self.message[COMMAND_TYPE_LOCATION + 1:]

    def __add__(self, other):
        if self.command_type != other.command_type:
            raise CommandTypesDontMatch()
        combined_message = self.command_data + other.command_data
        return CommandDataMessage(command_type=self.command_type, command_data=combined_message)
