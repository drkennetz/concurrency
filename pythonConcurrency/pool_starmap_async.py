import multiprocessing as mp

def power(x, y):
    return x**y

if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count()-1) as pool:
        async_result = pool.starmap_async(power, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
        # Blah, Blah, Blah do other stuff while mp tasks running
        result = async_result.get() # This blocks until results are ready
    print(result)
