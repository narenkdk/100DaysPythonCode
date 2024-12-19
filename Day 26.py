#Day 26 - Anagram strings

#Write a function check if two strings are anagrams.

def are_anagrams(string1, string2):
    """
    Check if two strings are anagrams.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Remove spaces and convert to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Compare sorted versions of the strings
    return sorted(string1) == sorted(string2)

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  # Output: True
