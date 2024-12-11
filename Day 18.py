#Day 18 - List Sum

#Write a function to find the sum of all elements 
# in a list.

def sum_of_elements(input_list):
    """
    Calculate the sum of all elements in a list.
    
    Parameters:
    input_list (list): A list of numbers.
    
    Returns:
    int/float: The sum of all elements in the list.
    """
    return sum(input_list)

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print(f"The sum of the list is: {result}")
