#Day 24 - Words to sentence.

#Write a function to convert a list of words into a sentence.

def list_to_sentence(word_list):
    """
    Converts a list of words into a properly formatted sentence.
    
    Args:
        word_list (list): A list of strings (words).
        
    Returns:
        str: A sentence formed by joining the words.
    """
    if not word_list:  # Check for an empty list
        return ""
    sentence = " ".join(word_list)  # Join words with spaces
    sentence = sentence.capitalize()  # Capitalize the first letter
    if not sentence.endswith("."):  # Add a period if not present
        sentence += "."
    return sentence

# Example usage
words = ["this", "is", "a", "simple", "sentence"]
print(list_to_sentence(words))  # Output: "This is a simple sentence."
