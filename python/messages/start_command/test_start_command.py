
from messages.start_command import StartCommandMessage


def test_start_command_message():
    """
    Checks that the api has not been broken on CommandDataMessage
    """
    type_and_data = StartCommandMessage(command_type=1, command_data="run command")
    assert type_and_data.message == b"\x01run command"
    message = StartCommandMessage(message=b"\x01run command")
    assert message.command_type == type_and_data.command_type
    assert message.command_data == type_and_data.command_data
