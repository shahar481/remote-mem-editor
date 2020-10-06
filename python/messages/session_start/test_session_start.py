import struct


from messages.session_start import SessionStartMessage


def test_session_start_message():
    """
    Checks that the api has not been broken on error messages
    """
    s = SessionStartMessage(struct.pack("!BBBBB", 1, 2, 3, 4, 5))
    assert s.supported_commands == (1,2,3,4,5)
