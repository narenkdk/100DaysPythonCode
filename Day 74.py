#Day 74: Natural language processing


#Perform natural language processing tasks (e.g., sentiment analysis).

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Example sentences
sentences = [
    "I love the new design of this app, it's amazing!",
    "This is the worst movie I've ever seen.",
    "The weather today is okay, nothing special."
]

# Analyze sentiment for each sentence
for sentence in sentences:
    sentiment = sia.polarity_scores(sentence)
    print(f"Sentence: {sentence}")
    print(f"Positive: {sentiment['pos']}, Neutral: {sentiment['neu']}, Negative: {sentiment['neg']}, Compound: {sentiment['compound']}\n")
