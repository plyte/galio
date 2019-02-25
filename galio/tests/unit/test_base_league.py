import galio
import pytest

@pytest.fixture
def test_league_instantiation():
    league = galio.League(api_key='dummy')
    return league
