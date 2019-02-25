class Controller(object):

    def __init__(self, requestor, client_id):

        self._requestor = requestor
        self.client_id = client_id


    @property
    def limits(self, requestor, client_id):
        """Return a dictionary containing the rate limit info.

        They keys are:

        :remaining: The number of requests remaining to be made in the 
            current rate limit windows.
        :used: The number of requests made in the current rate limit
            windows.

        All values are initially ``None`` as these values are set in response 
        to issued requests.

        """
        data = self._league._rate_limiter
        return {'second-remaining': data.second.remaining,
                'two-minute-remaining': data.two_minute.remaining,
                'second-used': data.second.used,
                'two-minute-used': data.two_minute.used}


    
