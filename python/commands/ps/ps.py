from commands.base import BaseCommand


COMMAND_TYPE = 1
PROCESS_SEPARATOR = b"\x00"


class Ps(BaseCommand):
    def __init__(self, networking):
        """
        A process list command
        :param networking: networking object
        """
        super().__init__(command_type=COMMAND_TYPE, networking=networking)

    def start(self):
        self._start_session(b"")
        output = self._recv_data_until_end_of_command_stream()
        return self._parse_output(output.command_data)

    def _parse_output(self, command_output):
        splitted = command_output.strip(PROCESS_SEPARATOR).split(PROCESS_SEPARATOR)
        processes = {}
        pid = -1
        for process in splitted:
            if pid == -1:
                pid = int(process)
            else:
                processes[pid] = process.decode("UTF-8")
                pid = -1
        return processes
