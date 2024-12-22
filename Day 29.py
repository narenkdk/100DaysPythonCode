#Day 29 - Words frequency

#Create a dictionary of words and their frequencies.

# Sample text
text = "This is a simple example to create a dictionary of words and their frequencies. This is simple!"

# Convert text to lowercase and remove punctuation
import string
cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))

# Split the text into words
words = cleaned_text.split()

# Create the dictionary of word frequencies
word_frequencies = {}
for word in words:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

# Print the dictionary
print(word_frequencies)
