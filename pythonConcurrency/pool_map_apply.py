import multiprocessing as mp

def square(x):
    return x**2

def cube(x):
    return x**3

if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count()-1) as pool:
        serial_cube = pool.apply(cube, (5,))
        parallel_square_map = pool.map(square, [1, 2, 3, 4, 5])
        # This will run each square as a separate process in the pool, but should not be
        # preferred over map or starmap.
        parallel_square_apply = [pool.apply(square, (i,)) for i in range(1, 6)]
        serial_square = pool.apply(square, (2,))
        parallel_cube = pool.map(cube, [1, 2, 3, 4, 5])
    print(f"serial cube: {serial_cube}")
    print(f"parallel square map: {parallel_square_map}")
    print(f"parallel square apply: {parallel_square_apply}")
    print(f"serial square: {serial_square}")
    print(f"parallel cube: {parallel_cube}")


