#Day 22 - List duplicates

def remove_duplicates(input_list):
    """
    Remove duplicates from a list while preserving the order of elements.

    Parameters:
        input_list (list): The list to process.

    Returns:
        list: A list with duplicates removed.
    """
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Example usage:
sample_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(sample_list)
print(unique_list)  # Output: [1, 2, 3, 4, 5]
