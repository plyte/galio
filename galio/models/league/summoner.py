from .base import Base
#from .arg_helper import ArgumentHelper
from ...const import API_PATH, region_code
from .exceptions import InvalidInvocation
#from ..helpers import ArgumentHelper

class Summoner(Base):
    
    def __init__(self, league, name=None, id=None, puuid=None, accountId=None, _data=None, region=None, *args, **kwargs):
        super(Summoner, self).__init__(league, _data, *args, **kwargs)

        if region is None or region not in (region_code.values() or region_code.keys()):
            raise InvalidInvocation('the region specified is not a valid region or formatted correctly.'
                                    'The regions allowed are as follows: {}'.format(
                                        ', '.join([str(x) for x in region_code.keys()]))
                                    )
        elif region in region_code.keys():
            self.region = region_code[region]
        elif region in region_code.values():
            self.region = region
            
        self._league = league
        self.name = name
        self.id = id
        self.puuid = puuid
        self.accountId = accountId

        api_path = self.base_uri.format(region=self.region) + API_PATH['summoner'][self._parse_input(name, id, puuid, accountId)]

        self._league.get(api_path)
    

    def _parse_input(self, name=None, id=None, puuid=None, accountId=None):

        if bool(name):
            return 'name'
        
        if bool(id):
            return 'summoner_id'
        
        if bool(accountId):
            return 'account_id'

        if bool(puuid):
            return 'puuid'
        
        
        