import time

def now_timestamp() -> int:
    """Return current timestamp in milliseconds."""
    return int(time.time() * 1000)