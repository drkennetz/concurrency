import multiprocessing as mp

def square(x):
    return x**2

def cube(x):
    return x**3

if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count()-1) as pool:
        serial_cube = pool.apply(cube, (5,))
        parallel_square = pool.map(square, [1, 2, 3, 4, 5])
        serial_square = pool.apply(square, (2,))
        parallel_cube = pool.map(cube, [1, 2, 3, 4, 5])
    print(f"serial cube: {serial_cube}")
    print(f"parallel square: {parallel_square}")
    print(f"serial square: {serial_square}")
    print(f"parallel cube: {parallel_cube}")


