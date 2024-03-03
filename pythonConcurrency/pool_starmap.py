import multiprocessing as mp

def power(x, y):
    return x ** y

if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count()-1) as pool:
        result = pool.starmap(power, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    print(result)
