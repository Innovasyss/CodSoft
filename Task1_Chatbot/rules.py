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

    "how_are_you": {
        "keywords": ["how are you", "how do you do", "how is it going"],
        "responses": [
            "I'm just a computer program, but I'm functioning perfectly!",
            "I'm doing great, thanks for asking!",
            "All systems operational!"
        ],
        "priority": 2
    },

    "joke": {
        "keywords": ["tell me a joke", "joke", "funny"],
        "responses": [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I would tell you a UDP joke, but you might not get it."
        ],
        "priority": 2
    },

    "creator": {
        "keywords": ["who created you", "who made you", "author"],
        "responses": [
            "I was created by Bhavesh Bansod as part of the CodSoft Internship.",
            "My creator is Bhavesh Bansod."
        ],
        "priority": 3
    },

    "age": {
        "keywords": ["how old are you", "your age"],
        "responses": [
            "I don't have an age, but I was built recently!",
            "I'm timeless, existing only in code."
        ],
        "priority": 2
    },

    "goodbye": {
        "keywords": ["bye", "exit", "quit"],
        "responses": [
            "Goodbye! Have a nice day.",
            "See you later!"
        ],
        "priority": 5
    },

    "time": {
        "keywords": ["what time is it", "current time", "time now"],
        "responses": [
            "I can't access the system clock here — please check your device for the current time.",
            "Check your system clock to see the current time."
        ],
        "priority": 2
    },

    "date": {
        "keywords": ["what's the date", "today's date", "date today"],
        "responses": [
            "I can't read the calendar right now; please check your device for today's date.",
            "Please check your system calendar for today's date."
        ],
        "priority": 2
    },

    "weather": {
        "keywords": ["weather", "how's the weather", "is it raining", "forecast"],
        "responses": [
            "I can't fetch live weather here. Tell me your city and I can suggest where to check.",
            "I don't have live weather access; try a weather website or app for a forecast."
        ],
        "priority": 3
    },

    "location": {
        "keywords": ["where are you", "where do you live", "location"],
        "responses": [
            "I'm a program running on your machine.",
            "I exist in code on your device."
        ],
        "priority": 3
    },

    "fallback": {
        "keywords": ["unknown", "??", "huh"],
        "responses": [
            "Sorry, I didn't understand that. Can you rephrase?",
            "I'm not sure I follow — could you say that differently?"
        ],
        "priority": 10
    },

    "compliment": {
        "keywords": ["good job", "well done", "nice", "great"],
        "responses": [
            "Thanks!",
            "Appreciate it!"
        ],
        "priority": 1
    },

    "complaint": {
        "keywords": ["not working", "this is bad", "bug", "error"],
        "responses": [
            "Sorry to hear that. Can you give more details so I can help?",
            "I understand there's an issue — please describe it and I'll try to assist."
        ],
        "priority": 2
    },

    "small_talk": {
        "keywords": ["what do you do", "hobbies", "what are your hobbies", "what can you do"],
        "responses": [
            "I chat and help with simple tasks and answers.",
            "I can respond to messages using predefined rules and try to assist."
        ],
        "priority": 3
    },

    "ask_help_specific": {
        "keywords": ["how to", "can you help me with", "show me how", "guide me"],
        "responses": [
            "Sure—tell me exactly what you need help with.",
            "I can try to help. What do you want to do?"
        ],
        "priority": 2
    },

    "repeat": {
        "keywords": ["say that again", "repeat", "can you repeat"],
        "responses": [
            "Which part should I repeat?",
            "I can repeat — what would you like me to say again?"
        ],
        "priority": 2
    },

    "affirmation": {
        "keywords": ["yes", "yeah", "yep", "sure", "ok", "okay"],
        "responses": [
            "Got it.",
            "Okay."
        ],
        "priority": 1
    },

    "negation": {
        "keywords": ["no", "nope", "nah"],
        "responses": [
            "Understood.",
            "Alright."
        ],
        "priority": 1
    },

    "language": {
        "keywords": ["do you speak", "speak english", "language"],
        "responses": [
            "I can communicate in English.",
            "I operate in English for now."
        ],
        "priority": 3
    },

    "preferences": {
        "keywords": ["what's your favorite", "favorite food", "favorite color"],
        "responses": [
            "I don't have personal preferences, I'm just code.",
            "I don't have favorites, but I can help you pick one!"
        ],
        "priority": 4
    }
}

