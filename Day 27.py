#Day 27 - Longest word

#Find the longest word in a sentence.

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

# Example usage
sentence = "Find the longest word in this sentence."
print("The longest word is:", find_longest_word(sentence))
