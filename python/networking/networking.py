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

    def is_connected(self):
        return self._connection_sock is not None

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

    def send_message(self, message):
        header = struct.pack("!IB", len(message.message) + 1, message.message_type)
        self._connection_sock.send(header + message)

    def send_and_wait_for_ack(self, message):
        """
        Sends a message and waits for a message to come back
        :param message: Message to send
        :return: Received message
        """
        self.send_message(message)
        return self.recv_message()


