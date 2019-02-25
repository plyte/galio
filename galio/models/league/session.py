from copy import deepcopy
import logging
import random
import time

from requests.compat import urljoin
from requests.exceptions import (ConnectionError)
from requests.status_codes import codes

from ...controller import Controller
from .exceptions import InvalidInvocation
from .rate_limiter import RateLimiter

log = logging.getLogger(__package__)

class Session(object):
    """Low level conntection interface to Riot's API."""

    @staticmethod
    def _log_request(data, method, params, url):
        log.debug('Fetching: {} {}'.format(method, url))
        log.debug('Data: {}'.format(data))
        log.debug('Params: {}'.format(params))

    
    @staticmethod
    def _retry_sleep(retries):
        if retries < 3: 
            base = 0 if retries == 2 else 2
            sleep_seconds = base + 2 * random.random() # fix
            message = 'Sleeping: {:0.2f} seconds prior to' \
                      ' retry'.format(sleep_seconds)
            log.debug(message)
            time.sleep(sleep_seconds)

    def __init__(self, controller):
        """Prepare the connection to Riot's API.

        :param controller: An instance of :class:`Controller`.

        """
        if not isinstance(controller, Controller):
            raise InvalidInvocation('invalid controleler {}'
                                    .format(controller))
        
        self._controller = controller
        self._rate_limiter = RateLimiter()
