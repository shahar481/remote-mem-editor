import logging


from decorators import is_connected
from networking import Networking
from messages.session_start import SessionStartMessage
from exceptions import UnexpectedMessageType
from commands.ps import Ps


SUPPORTED_COMMANDS = {1: Ps}


class MemEditor(object):
    def __init__(self, listen_ip, listen_port):
        """
        Main object for controlling the mem editor
        :param listen_ip: Ip to listen on
        :param listen_port: Port to listen on
        """
        self._networking = Networking(listen_ip, listen_port)
        self.listen_ip = self._networking.listen_ip
        self.listen_port = self._networking.listen_port
        self.supported_commands = []

    def wait_for_connection(self):
        """
        Waits for the client to connect
        """
        self._networking.wait_for_connection()

    @is_connected
    def _set_supported_commands(self):
        """
        Receives the supported commands from client
        """
        msg = self._networking.recv_message()
        if not isinstance(msg, SessionStartMessage):
            raise UnexpectedMessageType("Expected a start session message")
        self.supported_commands = msg.supported_commands
        readable_supported_commands = {}
        for command in self.supported_commands:
            if command not in SUPPORTED_COMMANDS:
                logging.error("Unsupported command-{0}".format(command))
            else:
                readable_supported_commands[command] = SUPPORTED_COMMANDS[command]

        logging.info("The client supports-{0}", readable_supported_commands)

    def ps(self):
        """
        Gets a process list from the client
        :return: Dict with {PID:CMDLINE}
        """
        p = Ps(self._networking)
        return p.start()





