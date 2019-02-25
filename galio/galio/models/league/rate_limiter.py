from functools import wraps
import math
import time


class RateLimitor():
    
    
    def __init__(self, rate, per, allowance, last_check=time.time(), name='default'):
        self.name = name
        self.rate = rate
        self.per = per
        self.allowance = allowance
        self.last_check = last_check
        self.last_reset = time.time()


    def _check_allowance(self):
        """Function that checks the allowance bucket if there are 
        enough tokens to allow for a function call.

        :returns: Boolean, whether or not the function is allowed to call at this point in time
        """
        current = time.time()
        time_passed = current - self.last_check
        self.last_check = current
        self.allowance += time_passed * (self.rate / self.per)
        
        if self.allowance > self.rate:
            self.allowance = self.rate
            
        if self.allowance < 1.0:
            return False
        else:
            self.allowance -= 1.0
            return True
        
        
    def __call__(self, f):

        @wraps(f)
        def wrapper(*args, **kwargs):
            
            if self._check_allowance():
                f(*args, **kwargs)
            else:
                print(self.name + " is sleeping for {} seconds".format(self._period_remaining()))
                
                time.sleep(self._period_remaining()) # get remaining time
                self.allowance = self.rate
                self.last_reset = time.time()
                
                f(*args, **kwargs)
                self.allowance -= 1
                
        return wrapper
    
    def _period_remaining(self):
        
        elapsed = time.time() - self.last_reset
        
        return math.fabs(self.per - elapsed)

        