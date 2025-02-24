#Day 93: Code Optimization


#Optimize code for performance (e.g., profiling, optimization techniques).

import cProfile
import numpy as np
from functools import lru_cache
import multiprocessing


# 1. Optimized Fibonacci using Memoization
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 2. Using NumPy for Faster Array Operations
def numpy_operations():
    arr = np.arange(1, 1000000)
    return arr ** 2  # Vectorized operation instead of looping


# 3. Generator for Memory Efficiency
def number_generator(n):
    for i in range(n):
        yield i


# 4. Multiprocessing for Faster Computation
def compute_square(n):
    return n * n


def parallel_processing():
    numbers = list(range(1, 1000000))
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_square, numbers)
    return results


# 5. Profiling Code Execution
def main():
    print("Fibonacci(30):", fibonacci(30))

    print("Performing NumPy Operations...")
    numpy_operations()

    print("Generating Numbers...")
    gen = number_generator(1000000)
    sum(gen)  # Consumes generator efficiently

    print("Running Parallel Processing...")
    parallel_processing()


if __name__ == "__main__":
    cProfile.run("main()")
