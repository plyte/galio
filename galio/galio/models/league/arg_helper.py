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