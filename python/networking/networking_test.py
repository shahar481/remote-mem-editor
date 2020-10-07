import _thread
import socket
import struct


from messages.session_start import SessionStartMessage
from networking import Networking


def test_networking():
    n = Networking("127.0.0.1", 0)
    _thread.start_new_thread(_handle_server, (n, ))
    n.wait_for_connection()
    # Full message
    msg = n.recv_message()
    assert isinstance(msg, SessionStartMessage)
    # Split message
    msg = n.recv_message()
    assert isinstance(msg, SessionStartMessage)


def _handle_server(networking_object):
    s = socket.socket()
    s.connect(("127.0.0.1", networking_object.listen_port))
    # Full message
    s.send(struct.pack("!IB", 5, 1) + "sdff".encode())
    # Split message
    s.send(struct.pack("!IB", 5, 1))
    s.send("sdff".encode())
