#Day 76: Chatbot


#Create a chatbot using NLP libraries.


#Basic Rule-Based Chatbot using NLTK

import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm good, how about you?", "I'm just a bot, but I'm doing fine!"]],
    [r"what is your name?", ["I'm a chatbot!", "You can call me ChatBot."]],
    [r"bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]],
    [r"(.*)", ["I'm not sure how to respond to that.", "Can you rephrase that?"]]
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")


