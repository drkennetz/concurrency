import multiprocessing as mp

def square(x):
    return x**2

if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count() - 1) as pool:
        async_result = pool.map_async(square, [1, 2, 3, 4, 5])
        # Blah, Blah, Blah, do other tasks while async is running
        result = async_result.get() # This is blocking
    print(result)
