# Parallel Processing in Python - A Practical Guide with Examples

Parallel processing is a mode of operation where the task is executed simultaneously in multiple processors.
It is meant to reduce the overall processing time by distributing work.

## Intro
There is overhead when communicating between processes which will increase overall time taken for small tasks.
The `multiprocessing` library is used to run independent parallel processes by using subprocesses (instead of threads)

It allows you to leverage multiple processors on a machine, which means the processes can be run in completely separate
memory locations.

## Check the total number of parallel processes you can run:
Max number of processes you can run at a time is limited by the number of processors in your computer. If you don't know
how many processors are present in the machine, the cpu_count() function in multiprocessing will show it. Jump over to `cpu_count.py` and run `python3 cpu_count.py`.
```bash
python3 cpu_count.py 
Number of processors: 12
```

## Synchronous and Asynchronous Execution
In parallel processing, there are two types of execution: Synchronous and Asynchronous (sync and async).

Synchronous execution is when the processes are completed in the same order in which it was started. This is achieved by locking the main program until the respective processes are finished.

Asynchronous execution doesn't involve locking. As a result, the order of results can get mixed up but may get done quicker.

Pool Class:
 - sync exec:
   - `Pool.map()` and `Pool.starmap()` - 
   - `Pool.apply()`
 - async exec:
   - `Pool.map_async()` and `Pool.starmap_async()`
   - `Pool.apply_async()`

### Sync Execution:
`Pool.map()`:
 - takes a function and an iterable as arguments
 - Applies the function to each element of the iterable one by one
 - Function should take only one argument
 - example in `pool_map.py`

`Pool.starmap()`:
 - takes a function and an iterable of argument tuples as arguments
 - It applies the function to each tuple in the iterable, unpacking the tuple as arguments to the function
 - The function should accept as many arguments as there are elements in each tuple
 - This is particularly useful when you have a function that requires multiple arguments and
   you want to apply it to a list of tuples where each tuple contains the arguments for one function call.
 - example in `pool_starmap.py`

`Pool.apply()`:
 - Not a parallel implementation (can use in a list to run multiple instantiations in parallel)
 - Applies a function to the arguments specified in args, like `apply(func, args=())`.
 - Executes the function with the provided arguments synchronously, meaning it awaits for the function call to complete
   before returning the result.
 - Allows us to keep sequential code within same pooling as parallel execution, providing easier interface integration,
   clearer code reading, and easier to refactor if algorithm eventually becomes parallelizable.
 - I do not know of any cases where one should call `Pool.apply()` in a list as opposed to `map()` or `starmap()`,
   but I will include an example.
 - Example in `pool_map_apply.py` -> shows how it can be a bit clearer with other parallel code execution.

### Async Execution
`map_async` and `starmap_async` are similar to `map` and `starmap` respectively, but they return asynchronous result objects immediately
instead of blocking until all results are ready. This allows you to continue with other tasks while the multiprocessing tasks are running
in the background.

`Pool.map_async()`:
 - applies a function to each item in an iterable asynchronously
 - takes the same arguments as `map()`: a func and an iterable
 - It returns an `AsyncResult` object immediately instead of blocking until all results are ready
 - Can use the `get()` method of `AsyncResult` object to retrieve the results when they are ready
 - Example in `pool_map_async.py`

`Pool.starmap_async()`:
 - `starmap_async()` applies in same way as `starmap` and has same behavior as `map_async()`
 - Example in `pool_starmap_async.py`

`Pool.apply_async()`:
 - sorry for the brevity - applies in the same way as `apply` and has same behavior as other async methods
 - Example in `pool_apply_async.py`

## Count numbers between a given range in each row - parallel example problem
The first problem is: Given a 2D matrix, count how many numbers are present between a given range in each row.
We will explore this in `matrix.py`

