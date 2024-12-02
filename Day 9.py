#Day 9 - Random number generator

#Q. 1. Write a program that generates a random 
# number.

import random


random_number = random.random()  # This generates a float between 0.0 and 1.0
print("Random number:", random_number)


#Q. 2. Write a program that generates random number 
# between 2 integers
 
import random

# Set the range
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))


random_number = random.randint(low, high)  # Includes both low and high
print(f"Random number between {low} and {high}: {random_number}")
