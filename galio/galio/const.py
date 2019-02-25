import sys
import os

__version__ = '0.1'
api_version = 'v4'

API_PATH = {
    'summoner': {
        'name': 'summoner/{version}/summoners/by-name/{{encryptedAccountId}}'.format(version=api_version),
        'accountId': 'summoner/{version}/summoners/by-account/{{name}}'.format(version=api_version),
        'puuid': 'summoner/{version}/summoners/by-puuid/{{puuid}}'.format(version=api_version),
        'id': 'summoner/{version}/summoners/{{id}}'.format(version=api_version)
    },

    'match': {
        'matches': 'match/{version}/matches/{{match_id}}'.format(version=api_version),
        'matchlists': 'match/{version}/matchlists/by-account/{{account_id}}'.format(version=api_version),
        'timelines': 'match/{version}/by-match/{{match_id}}'.format(version=api_version),
        'tournament-code': {
            'by-tournament-code': 'match/{version}/matches/by-tournament-code/{{tournament_code}}/ids'.format(version=api_version),
            'by-match-and-tournament-code': '/match/{version}/matches/{{match_id}}/by-tournament-code/{{tournament_code}}'.format(version=api_version)
        }
    },

    'leagues': {
        'challenger-by-queue': 'league/{version}/challengerleagues/by-queue/{{queue}}'.format(version=api_version),
        'grandmaster-by-queue': 'league/{version}/grandmasterleagues/by-queue/{{queue}}'.format(version=api_version),
        'by-league': 'league/{version}/leagues/{{league_id}}'.format(version=api_version),
        'masterleagues-by-queue': 'league/{version}/masterleagues/by-queue/{{queue}}'.format(version=api_version),
        'positional-rank-queues': 'league/{version}/positional-rank-queues'.format(version=api_version),
        'positions-by-summonerId': 'league/{version}/positions/by-summoner/{{summoner_id}}'.format(version=api_version),
        'positional-league-entires': 'league/{version}/positions/{{positional_queue}}/{{tier}}/{{division}}/{{position}}/{{page}}'.format(version=api_version)
    },

    'spectator': {
        'by-summonerId': 'spectator/{version}/active-games/by-summoner/{{summoner_id}}'.format(version=api_version),
        'featured-games': 'spectator/{version}/featured-games'.format(version=api_version)
    }
}

region_code = {'BR': 'br1',
               'EUNE': 'eun1',
               'EUW': 'euw1',
               'JP': 'jp1',
               'KR': 'kr',
               'LAN': 'la1',
               'LAS': 'la2',
               'NA': 'na1',
               'OCE': 'oc1',
               'TR': 'tr1',
               'RU': 'ru',
               'PBE': 'pbe1'
              }

USER_AGENT_FORMAT = '{{}} galio/{}'.format(__version__)
TIMEOUT = float(os.environ.get('prawcore_timeout', 16))

if sys.version_info.major == 2:
    import ConfigParser as configparser
    from urlparse import urljoin, urlparse
else:
    import configparser
    from urllib.parse import urljoin, urlparse