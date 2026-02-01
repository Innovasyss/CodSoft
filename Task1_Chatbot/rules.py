# rules.py
# Defines intents, keywords, and responses

RULES = {
    "greeting": {
        "keywords": ["hi", "hello", "hey"],
        "responses": [
            "Hello! How can I help you?",
            "Hi there! What can I do for you?",
            "Hey! Need any help?"
        ],
        "priority": 1
    },

    "ask_name": {
        "keywords": ["your name", "who are you"],
        "responses": [
            "I am a rule-based chatbot.",
            "I'm a simple chatbot built using Python."
        ],
        "priority": 2
    },

    "help": {
        "keywords": ["help", "commands"],
        "responses": [
            "You can greet me, ask my name, or type exit to quit.",
            "Try saying hello, asking my name, or typing exit."
        ],
        "priority": 3
    },

    "thanks": {
        "keywords": ["thank you", "thanks"],
        "responses": [
            "You're welcome!",
            "Glad I could help!"
        ],
        "priority": 1
    },

    "set_name": {
        "keywords": ["my name is"],
        "responses": [
            "Nice to meet you, {name}!",
            "Hello {name}, nice to meet you!"
        ],
        "priority": 4
    },

    "get_name": {
        "keywords": ["what is my name", "do you know my name"],
        "responses": [
            "Your name is {name}.",
            "You told me your name is {name}."
        ],
        "priority": 4
    },


    "goodbye": {
        "keywords": ["bye", "exit", "quit"],
        "responses": [
            "Goodbye! Have a nice day.",
            "See you later!"
        ],
        "priority": 5
    }
}
