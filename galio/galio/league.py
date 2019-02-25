from .const import API_PATH, __version__, USER_AGENT_FORMAT
from .objector import Objector
from .requestor import Requestor
from .controller import Controller
from .models.league.config import Config
from . import models

import requests

class League(object):

    def __enter__(self):
        return self


    def __exit__(self):
        pass

    def __init__(self, api_key, requestor_class=None, requestor_kwargs=None, 
                 user_agent=None, **config_settings):
        """Initialize a League instance

        :param api_key: The api key that riot gives you when you signup
            for a development key.
        :param requestor_class: A class that will be used to create a 
            requestor. If not set, use ``Base.Requestor`` (default: None)
        :param requestor_kwargs: Dictionary with additional keyword 
            arguments used to initialize the requestor (default:None)

        """
        self.api_key = api_key
        self._objector = None
        self._controller = None
        self.user_agent = None
        self.config = Config(api_key, **config_settings)

        required_message = ('Required configuration setting {!r} missing. \n',
                            'This setting is intended to be provided '
                            'as a keyword argument to the `League` class constructor')
        for attribute in ('api_key', 'user_agent'):
            if getattr(self.config, attribute) is None:
                raise ClientException(required_message.format(attribute))

        self._prepare_objector()
        self._prepare_requestor(requestor_class)

        self.summoner = models.SummonerHelper(self, None)
        """An instance of :class:`Summoner`.

        Provides the interface for interacting with summoner data. For 
        example:

        .. code-block:: python

            leauge.summoner('RiotSchmick')

        Apart from using the username, you can also use the summoner_id, puuid, or the account_id.
        If you wish to use these make sure to include the keyword argument for that case.
        For example:

        .. code-block:: python

            league.summoner(summoner_id=<the user's id>)

        """


    def _prepare_requestor(self, requestor_class=None, requestor_kwargs=None):

        requestor_class = requestor_class or Requestor
        requestor_kwargs = requestor_kwargs or {}

        requestor = requestor_class(
            USER_AGENT_FORMAT.format(self.config.user_agent or 'galio bot 1')
        )

        if self.config.api_key :
            self._prepare_controller(requestor)


    def _prepare_controller(self, requestor):

        controller_class = Controller(requestor)

        self._controller = controller_class



    def _prepare_objector(self):
        self._objector = Objector(self)
        mappings = {'Summoner': models.Summoner}

        for kind, klass in mappings.items():
            self._objector.register(kind, klass)


    @property
    def _requestor(self):
        return self._controller._requestor

    
    def close(self):
        """Close the session and perform any clean up"""
        self._requestor.close()


    def request(method, path, params=None):
        """Return the parsed JSON data returned from a request of a URL.

        :param method: The HTTP method (e.g., GET, POST, PUT, DELETE).
        :param path: The path to fetch.
        :param params: The query parameters to add to the request (default:
            None).
        :return: A python dictionary containing the data 
        
        """

        params = deepcopy(params) or {}
        params['raw_json'] = 1
        if isinstance(data, dict):
            data = deepcopy(data)
            data['api_type'] = 'json'
            data = sorted(data.items())
        url = urljoin(self._requestor.url, path)
        return self._request_with_retries(
            data=data,
        )


    def get(self, path, params=None):
        """Return a parsed object returned from the data from 
        a GET request to ``path``/

        :param path: The path to fetch
        :param params: The query parameters to add to the request (default: None)

        """
        data = self._requestor.request('GET', path, params=params)
        return self._objector.objectify(data)
    