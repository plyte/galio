class _NotSet(object):

    def __bool__(self):
        return False

    __nonzero__ = __bool__
    
    def __str__(self):
        return 'NotSet'

class ArgumentHelper(object):

    ARG_NOT_SET = _NotSet()

    def __init__(self, attributes, **arguments):
        self._attributes = attributes
        self._arguments = arguments

        self._initialize_attributes()

    def _initialize_attributes(self):

        for attribute in self._attributes:
            setattr(self, attribute, self._fetch_or_not_set(attribute))

    def _fetch(self, key):
        value = self._arguments[key]
        del self._arguments[key]
        return value

    def _fetch_or_not_set(self, key):
        if key in self._arguments:
            return self._fetch(key)

        return self.ARG_NOT_SET

class Base(object):
    
    def __init__(self, league, _data, database_filename=None):
        """Return an instance of :class:`~.Base`.
        
        :params league: The instance of :class:`~.League`.
        :params _data: A Dictionary containing data to be set as an object
        :params database_filename: The name of the database to be passed to
                                   generate a key name pair from sqlitedict.
                                   
        """
        self._league = league

        if _data:
            for attribute, value in _data.items():
                setattr(self, attribute, value)
        
        self.database_filename = database_filename
        self.api_key = self._league.api_key
        self.base_uri = 'https://{region}.api.riotgames.com/lol/',
        
        if self.database_filename is not None: self.my_dict = SqliteDict(self.database_filename) 
        
        
    def _handle_exception(self, error_code):
        
        e = ErrorHandler(error_code)
        e.throw_error()
        

    @classmethod
    def parse(cls, data, league):
        """Return an instance of ``cls`` from ``data``.

        :param data: The structured data.
        :param league: An instance of :class:`.League`.

        """
        return cls(league, _data=data)