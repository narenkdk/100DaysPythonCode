#Day 90: Concurrency and parallelism


#Explore concurrency and parallelism with Python (e.g., threading, multiprocessing).

#Concurrency with threading (For I/O-bound tasks)

import threading
import time

def worker(task_id):
    print(f"Task {task_id} started.")
    time.sleep(2)  # Simulating an I/O task
    print(f"Task {task_id} completed.")

# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All tasks completed.")


#Parallelism with multiprocessing (For CPU-bound tasks)
import multiprocessing
import time

def heavy_computation(n):
    print(f"Computing factorial of {n}")
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n}: {fact}")

if __name__ == "__main__":
    numbers = [10_000, 20_000, 30_000, 40_000]
    
    # Using multiprocessing for parallel execution
    processes = []
    for num in numbers:
        process = multiprocessing.Process(target=heavy_computation, args=(num,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All computations completed.")


