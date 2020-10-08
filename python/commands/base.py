from messages import StartCommandMessage
from messages import CommandDataMessage
from messages import ErrorMessage
from commands.decorators import validate_session_started


from abc import ABC, abstractmethod


class BaseCommand(ABC):
    """
    Abstract class which all commands inherit from
    """

    def __init__(self, command_type, networking):
        self.command_type = command_type
        self.networking = networking
        self._session_started = False

    @abstractmethod
    def start(self):
        """
        Starts the command and sends data
        """
        pass

    def _is_session_started(self):
        """
        Checks if the session has been started with the start_session function
        :return: Boolean
        """
        return self._session_started

    def _start_session(self, data):
        """
        Starts a command session with the start command
        :param data: Data of the command
        :return: None
        """
        start_command = StartCommandMessage(command_type=self.command_type, command_data=data)
        self.networking.send_and_wait_for_ack(start_command)
        self._session_started = True

    @validate_session_started
    def _send_data(self, data):
        """
        Sends continuation data with the command data message
        :param data: data to send
        :return: None
        """
        command_data = CommandDataMessage(command_type=self.command_type, command_data=data)
        self.networking.send_message(command_data)

    @validate_session_started
    def _end_session(self):
        """
        Ends the command session by sending an empty error message
        :return: None
        """
        end_command = ErrorMessage()
        self.networking.send_message(end_command)
        self._session_started = False

    def _recv_data_until_end_of_command_stream(self):
        """
        Receives data until an empty error is received
        :return: Received message
        """
        combined_command = CommandDataMessage(command_type=self.command_type, command_data=b"")
        received = self.networking.recv_message()
        while not isinstance(received, ErrorMessage):
            combined_command += received
            received = self.networking.recv_message()
        return combined_command
