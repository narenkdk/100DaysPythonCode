#Day 81: Tasks Scheduler


#Schedule tasks using the schedule library.

import schedule
import time

# Define tasks
def task1():
    print("Task 1 executed")

def task2():
    print("Task 2 executed")

# Schedule tasks
schedule.every(10).seconds.do(task1)  # Runs every 10 seconds
schedule.every().hour.do(task2)       # Runs every hour

# Keep running the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep to prevent high CPU usage
