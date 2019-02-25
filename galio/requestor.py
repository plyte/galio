from .models.league.exceptions import RequestException, InvalidInvocation
from .models.league.rate_limiter import RateLimitor
from .const import __version__, TIMEOUT, region_code
import requests

class Requestor(object):

    def __init__(self, user_agent, 
                 session=None):
        """Create an instance of :class:`Requestor`.

        :param session: (Optional) A session to handle requests, compatible
            with requests.Session(). (Default: None)
        :param region: (Optional) The region for which to query on for the particular 
            summoner. If the player is not in NA this value needs to be changed. (Default: 'na1')
        :param league_url: (Optional) The base url for the lol api including the region.
            (Default: https://na1.api.riotgames.com/lol/)

        """
        if user_agent is None or len(user_agent) < 7:
            raise InvalidInvoation('user_agent is not descriptive')

        self._http = session or requests.Session()
        self._http.headers['User-Agent'] = '{} galio/{}'.format(
            user_agent, __version__
        )

    def close(self):
        """Call close on the underlying session."""
        return self._http.close()

    
    def request(self, *args, **kwargs):
        """Issue the HTTP request capturing any errors that may occur."""
        try: 
            return self._http.request(*args, timeout=TIMEOUT, **kwargs)
        except Exception as exc:
            raise RequestException(exc, args, kwargs)



