#Day 36 - Handle Exceptions I

#Handle exceptions for division by zero.

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of dividing {a} by {b} is {result}.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        print("Division was successful.")
    finally:
        print("Operation complete.")

# Test cases
divide_numbers(10, 2)   # Valid division
divide_numbers(10, 0)   # Division by zero
divide_numbers(10, "a") # Invalid input type
