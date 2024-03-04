import time
from functools import wraps
import multiprocessing as mp
import numpy as np

def timer(name):
    def dec(func):
        @wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()  # Start the timer
            result = func(*args, **kwargs)
            end_time = time.perf_counter()    # Stop the timer
            execution_time = end_time - start_time
            print(f"Function {name} '{func.__name__}' executed in {execution_time:.4f} seconds")
            return result
        return wrapper_timer
    return dec

@timer("Serial non-vectorized")
def non_vec_count_between_min_max(arr, min_val, max_val):
    """ Count between min and max using loops """
    count = 0
    for row in arr:
        for ele in row:
            if min_val <= ele <= max_val:
                count += 1
    return count

@timer("Parallel non-vectorized")
def parallel_non_vec_count(chunk, min_val, max_val, procs=1):
    with mp.Pool(processes=procs) as pool:
        counts = pool.starmap(non_vec_count_between_min_max, [(chunk, min_val, max_val) for chunk in chunks])
    return sum(counts)

@timer("Serial vectorized")
def count_between_min_max(arr, min_val, max_val):
    """ Count numbers between min and max in array. """
    mask = (arr >= min_val) & (arr <= max_val)
    return np.count_nonzero(mask)

@timer("Parallel")
def parallel_count_min_max(chunks, min_val, max_val, procs=1):
    """ Chunk arr based on num procs, and count each chunk """
    with mp.Pool(processes=procs) as pool:
        counts = pool.starmap(count_between_min_max, [(chunk, min_val, max_val) for chunk in chunks])
    
    return np.sum(counts)

if __name__ == "__main__":
    np.random.RandomState(100)
    # Create 2000k rows of len 5 with random nums 0-10 (or 9, I don't remember if upper is inclusive.)
    arr = np.random.randint(0, 10, size=[20000000, 5])
    # Split array as I would work on each piece in parallel (creates views)
    chunks = np.array_split(arr, 4)
    non_vec_count_between_min_max(arr, 2, 8)
    parallel_non_vec_count(arr, 2, 8, 4)
    count_between_min_max(arr, 2, 8)
    parallel_count_min_max(chunks, 2, 8, 4)
