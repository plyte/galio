import galio
import pytest

@pytest.fixture
def test_summoner_instantiation():
    league = galio.League(api_key='dummy', requestor_class=None)
    return league

def test_summoner_name_call(test_summoner_instantiation):
    league = test_summoner_instantiation
    with pytest.raises(galio.models.league.exceptions.InvalidInvocation):
        summoner = league.summoner('dummy')
    #assert summoner.name == 'dummy'
