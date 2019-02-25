from galio import League

class UnitTest(object):
    """Base class for galio unit tests."""

    def setup(self):
        """Setup runs before all test cases."""
        self.league = League(api_key='dummy')