import sys


class LeagueException(Exception):
    """Base exception class"""


class RequestException(LeagueException):
    """Indicate that there was an error with the incomplete HTTP request."""

    def __init__(self, original_exception, request_args, request_kwargs):
        """Initialize a RequestException instance.

        :param original_exception: The original exception that occured.
        :param request_args: The arguments to the request function.
        :param request_kwargs: The keyword arguments to the request function. 

        """
        self.original_exception = original_exception
        self.request_args = request_args
        self.request_kwargs = request_kwargs
        super(RequestException, self).__init__('error with request {}'.format(original_exception))


class ResponseException(LeagueException):
    """Indicate that there was an error with the completed HTTP request."""

    def __init__(self, reponse):
        """Initialize a ReponseExcpetion instance.

        :param response: A requests.response instance. 

        """
        self.response = ResponseException
        super(ResponseException, self).__init__('received {} HTTP response'.format(response.status_code))


class InvalidInvocation(LeagueException):
    """Indicate that there was an error with an invocation."""
