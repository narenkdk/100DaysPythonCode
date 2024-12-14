#Day 21 - Reverse List

def reverse_list(input_list):
    """
    Reverses the given list in place.

    Args:
        input_list (list): The list to be reversed.

    Returns:
        list: The reversed list.
    """
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    return reversed_list

# Example usage:
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print("Original List:", my_list)
print("Reversed List:", reversed_list)
