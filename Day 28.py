#Day 28 - Reverse words

#Reverse words in a sentence.

def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Test the function
sentence = "Hello world, this is a test"
reversed_sentence = reverse_words(sentence)
print("Original Sentence:", sentence)
print("Reversed Sentence:", reversed_sentence)
