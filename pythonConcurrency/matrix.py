import time
from functools import wraps

import numpy as np

# Our timer decorator.
def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        result = func(*args, **kwargs)
        end_time = time.perf_counter()    # Stop the timer
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper_timer

def count_between_min_max(arr, min_val, max_val):
    """ Count numbers between min and max in array. """
    mask = (arr >= min_val) & (arr <= max_val)
    return np.count_nonzero(mask)

@timer
def serial_count(arr):
    pass

if __name__ == "__main__":
    # prep data
    np.random.RandomState(100)
    # Create 200k rows of len 5 with random nums 0-10 (or 9, I don't remember if upper is inclusive.)
    arr = np.random.randint(0, 10, size=[200000, 5])
