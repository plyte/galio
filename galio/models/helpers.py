from .league.base import Base
from .league.summoner import Summoner

class SummonerHelper(Base):

    def __call__(self, *args, **kwarg):
        """Return a new lazy instance of :class:`~.Summoner`.

        This method is intended to be used as:

        .. code:: python

            summoner = galio.summoner(summoner_name='RiotSchmick')

        :param username: The username of the individual you wish to lookup, e.g., ``RiotSchmick``.
        """
        return Summoner(self._league, *args, **kwarg)

