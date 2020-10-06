
from messages.command_data import CommandDataMessage
from messages.error import ErrorMessage
from messages.session_start import SessionStartMessage
from messages.start_command import StartCommandMessage


MESSAGE_TYPE_INDEX = 0
MESSAGE_TYPES = {1: SessionStartMessage, 2: ErrorMessage, 3: StartCommandMessage, 4: CommandDataMessage}


def parse_message(message):
    """
    Parses a message(without the length) and returns the correct class for that message
    :param message: Message to parse
    :return: One of the message classes that inherit from BaseMessage
    """
    message_type = message[MESSAGE_TYPE_INDEX]
    return MESSAGE_TYPES[message_type](message)

