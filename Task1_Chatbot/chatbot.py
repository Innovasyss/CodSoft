# chatbot.py
# CodSoft AI Internship - Task 1
# Advanced Rule-Based Chatbot

import random
import re

from utils import preprocess_text
from rules import RULES


def get_best_intent(user_input):
    """
    Find the best matching intent based on:
    - Keyword match score
    - Intent priority
    """
    best_intent = None
    best_score = 0
    best_priority = -1

    for intent, data in RULES.items():
        score = 0
        for keyword in data["keywords"]:
        
            if re.search(r"\b" + re.escape(keyword) + r"\b", user_input):
                score += 1

        if score > 0:
            if (score > best_score) or (
                score == best_score and data["priority"] > best_priority
            ):
                best_score = score
                best_priority = data["priority"]
                best_intent = intent

    return best_intent


def chatbot():
    print("Chatbot: Hello! I am an advanced rule-based chatbot.")
    print("Chatbot: Type 'exit' to end the conversation.\n")

    memory = {}

    while True:
        user_input = input("You: ")
        processed_input = preprocess_text(user_input)

        intent = get_best_intent(processed_input)

        if intent == "goodbye":
            response = random.choice(RULES[intent]["responses"])
            print(f"Chatbot: {response}")
            break

        elif intent == "set_name":
            name = processed_input.replace("my name is", "").strip()
            if name:
                memory["user_name"] = name.title()
                response = random.choice(RULES[intent]["responses"])
                print(f"Chatbot: {response.format(name=memory['user_name'])}")
            else:
                print("Chatbot: I didn't catch your name.")

        elif intent == "get_name":
            if "user_name" in memory:
                response = random.choice(RULES[intent]["responses"])
                print(f"Chatbot: {response.format(name=memory['user_name'])}")
            else:
                print("Chatbot: I don't know your name yet.")

        elif intent:
            response = random.choice(RULES[intent]["responses"])
            print(f"Chatbot: {response}")

        else:
            print("Chatbot: Sorry, I didn't understand that. Try typing 'help'.")

if __name__ == "__main__":
    chatbot()
