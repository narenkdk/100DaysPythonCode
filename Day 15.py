#Day 15 - Factorial

#Write a function to calculate the factorial of a 
# number.

def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): A non-negative integer

    Returns:
    int: Factorial of the number
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
try:
    number = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {number} is {factorial(number)}")
except ValueError as e:
    print(e)
