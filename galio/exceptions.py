class Base(Exception):
    """Base exception that all other exception classes extend."""


class APIException(Base):
    """Class to indicate exception that involve responses from Riot's API."""


    def __init__(self, error_type, message, field):
        """Initialize an instance of APIException.

        :param error_type: The error type set of Riot's end.
        :param message: The associated message for the error.
        :param field: The input field associated with the error if available.

        """
        error_str = u'{}: \'{}\''.format(error_type, message)
        if field:
            error_str += u' on field \'{}\''.format(field)
        error_str = error_str.encode('uncode_escape').decode('ascii')

        super(APIException, self).__init__(error_str)
        self.error_type = error_type
        self.message = message
        self.field = field


class ClientExcpetion(Base):
    """Indicate excpetions that don't involve interaction with Riot's API."""