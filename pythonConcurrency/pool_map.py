import multiprocessing as mp

def square(x):
    return x**2

if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count()-1) as pool:
        result = pool.map(square, [1, 2, 3, 4, 5])
    print(result)
