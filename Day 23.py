#Day 23 - List intersection

#Write a function to find the intersection of two lists.

def list_intersection(list1, list2):
    """
    Find the intersection of two lists.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list containing the common elements of both lists.
    """
    # Convert to sets to find the common elements
    return list(set(list1) & set(list2))

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = list_intersection(list1, list2)
print(intersection)  # Output: [4, 5]
