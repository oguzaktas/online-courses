import signal
from functools import wraps

def raise_timeout(*args, **kwargs):
    raise TimeoutError()

# When an "alarm" signal goes off, call raise_timeout()
signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)

# Set off an alarm in 5 seconds
signal.alarm(5)

# Cancel the alarm
signal.alarm(0)

def timeout_in_5s(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Set an alarm in 5 seconds
        signal.alarm(5)
        try:
            # Call the decorated func
            return func(*args, **kwargs)
        finally:
            # Cancel alarm
            signal.alarm(0)
    return wrapper

@timeout_in_5s
def foo():
    time.sleep(10)
    print('foo!')