from threading import Lock
import configparser

class _NotSet(object):

    def __bool__(self):
        return False

    __nonzero__ = __bool__

    def __str__(self):
        return 'NotSet'


class Config(object):

    CONFIG_NOT_SET = _NotSet()

    def __init__(self, api_key, **settings):
        """Load an instance of :class:`Config`."""

        self._settings = settings
        self.api_key = api_key

        self._initialize_attributes()

    def _fetch(self, key):
        value = self._settings[key]
        del self._settings[key]
        return value

    def _fetch_or_not_set(self, key):
        if key in self._settings:
            return self._fetch(key)

        return self.CONFIG_NOT_SET

    def _initialize_attributes(self):

        for attribute in ('user_agent',):
            setattr(self, attribute, self._fetch_or_not_set(attribute))
