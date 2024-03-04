import multiprocessing as mp

def square(x):
    return x**2

if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count() - 1) as pool:
        async_result = pool.apply_async(square, (5,))
        # Do other tasks while the function call is running.
        print("Other awesome stuff is going on while square(5) is running.")
        
        # Get the result of the async call, which is now blocking.
        result = async_result.get()
    
    print(f"Result of square(5): {result}")
