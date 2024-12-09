#Day 16 - Palindrome String

#Write a function to check if a given string is a 
# palindrome.

def is_palindrome(s):
    """
    Check if a given string is a palindrome.
    
    Args:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = ''.join(c.lower() for c in s if c.isalnum())
    # Compare the string with its reverse
    return s == s[::-1]

# Example usage
test_string = "A man, a plan, a canal, Panama!"
print(is_palindrome(test_string))  # Output: True
