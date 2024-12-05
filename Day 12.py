#Day 12 - Odd-even

#Q. Write a program to check if a number is even or 
# odd.

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "The number is Even."
    else:
        return "The number is Odd."

# Input from user
try:
    num = int(input("Enter a number: "))
    print(check_even_odd(num))
except ValueError:
    print("Please enter a valid integer.")
