import socket
from decorators import is_connected


class MemEditor(object):
    def __init__(self, listen_ip, listen_port):
        """
        Main object for controlling the mem editor
        :param listen_ip: Ip to listen on
        :param listen_port: Port to listen on
        """
        self.listen_ip = listen_ip
        self.listen_port = listen_port
        self._server_sock = socket.socket()
        self._connection = None
        self.supported_commands = []

    def wait_for_connection(self):
        """
        Waits for the client to connect
        """
        self._server_sock.bind((self.listen_ip, self.listen_port))
        self._server_sock.listen(1)
        self._connection = self._server_sock.accept()

    @is_connected
    def _set_supported_commands(self):
        """
        Receives the supported commands from client
        """
        pass




