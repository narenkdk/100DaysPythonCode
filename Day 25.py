#Day 25 - Words frequency

#Write a function to count the frequency of words in a sentence.

from collections import Counter

def word_frequency(sentence):
    """
    Counts the frequency of words in a sentence.

    Parameters:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    # Normalize the sentence to lowercase and split it into words
    words = sentence.lower().split()
    
    # Remove punctuation from words
    words = [word.strip(",.!?;:") for word in words]
    
    # Count word frequencies using Counter
    frequency = Counter(words)
    
    return frequency

# Example usage
sentence = "This is a test. This test is only a test."
print(word_frequency(sentence))
