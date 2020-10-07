import socket
import struct

from messages import parse_message

MESSAGE_LENGTH_SIZE = 4
RECV_SIZE = 1024


class Networking(object):
    def __init__(self, listen_ip, listen_port):
        self.listen_ip = listen_ip
        self.listen_port = listen_port
        self._listen_sock = socket.socket()
        self._connection_sock = None
        self._init_sock()

    def _init_sock(self):
        self._listen_sock.bind((self.listen_ip, self.listen_port))
        self._listen_sock.listen(1)
        self.listen_ip = self._listen_sock.getsockname()[0]
        self.listen_port = self._listen_sock.getsockname()[1]

    def wait_for_connection(self):
        self._connection_sock, _ = self._listen_sock.accept()

    def recv_message(self):
        length = self._connection_sock.recv(MESSAGE_LENGTH_SIZE)
        length = struct.unpack("!I", length)[0]
        received_buff = b""
        while len(received_buff) < length:
            temp_buff = self._connection_sock.recv(RECV_SIZE)
            received_buff += temp_buff
        return parse_message(received_buff)

