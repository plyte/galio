class Objector(object):

    def __init__(self, league):
        """Initialize an Objector instance.

        :param league: An of instance of :class: `~.League`.

        """
        self.parsers = {}
        self._league = league

    def _objectify_dict(self, data):
        """Create Base objects from dicts.

        :param data: The structured data, assumed to be a dict.
        :returns: An instance of :class:`~.Base`.

        """

        if {'id', 'accountId', 'puuid', 'name'}.issubset(data):
            parser = self.parsers['Summoner']

        return parser.parse(data, self._league)


    def objectify(self, data):
        """Create Base objects from data.

        :param data: The structured data.
        :returns: An instance of :class:`~.Base`, or ``None`` if 
            given ``data`` is ``None``.

        """

        if data is None:
            return None
        if isinstance(data, dict):
            return self._objectify_dict(data)

    def register(self, kind, cls):
        """Register a class for a given kind.

        :param kind: The kind in the parsed data to map to ``cls``.
        :param cls: A type of Base class.

        """
        self.parsers[kind] = cls