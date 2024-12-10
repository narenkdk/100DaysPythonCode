#Day 17 - Number of vowels in a string

#Write a function to count the number of vowels in a string.

def count_vowels(string):
    """
    Counts the number of vowels in the given string.

    Parameters:
        string (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

# Example usage
input_string = "Hello, World!"
print(f"Number of vowels: {count_vowels(input_string)}")
