#Day 19 - Maximum in List

#Write a function to find the maximum element in a list.

def find_maximum(lst):
    """
    Finds the maximum element in a list using the built-in max function.

    Parameters:
        lst (list): A list of numbers.

    Returns:
        max_element: The maximum element in the list.
        If the list is empty, returns None.
    """
    return max(lst) if lst else None

# Example usage:
numbers = [3, 5, 7, 2, 8]
print("The maximum element is:", find_maximum(numbers))
