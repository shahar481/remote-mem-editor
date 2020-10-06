import pytest

from exceptions import ErrorMessageReceived
from messages.error import ErrorMessage


def test_error_message():
    """
    Checks that the api has not been broken on error messages
    """
    with pytest.raises(ErrorMessageReceived):
        ErrorMessage("This is an error message")
