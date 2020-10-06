import pytest
import struct

from messages import parse_message
from messages import CommandDataMessage
from messages import SessionStartMessage
from messages import StartCommandMessage
from exceptions import ErrorMessageReceived


def test_parse_message_session_start():
    raw_message = struct.pack("B", 1) + "asdfasdf".encode()
    parsed = parse_message(raw_message)
    assert isinstance(parsed, SessionStartMessage)


def test_parse_message_error():
    with pytest.raises(ErrorMessageReceived):
        raw_message = struct.pack("B", 2) + "asdfasdf".encode()
        parse_message(raw_message)


def test_parse_message_start_command():
    raw_message = struct.pack("!BBBBBB", 3, 1, 2, 3, 4, 5)
    parsed = parse_message(raw_message)
    assert isinstance(parsed, StartCommandMessage)


def test_parse_message_command_data():
    raw_message = struct.pack("B", 4) + "asdfasdf".encode()
    parsed = parse_message(raw_message)
    assert isinstance(parsed, CommandDataMessage)
