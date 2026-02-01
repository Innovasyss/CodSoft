# Rule-Based Chatbot (Python)

## CodSoft Artificial Intelligence Internship – Task 1

This project implements an advanced **rule-based chatbot** using Python.  
The chatbot responds to user input based on predefined rules, keyword pattern matching, and simple conversational context, without using machine learning or external NLP libraries.

---

## 📌 Project Objective

To build a chatbot that:
- Uses **if-else logic and pattern matching**
- Identifies user intent based on predefined rules
- Demonstrates basic **natural language processing concepts**
- Maintains a simple conversation flow

This project strictly follows the requirements provided by CodSoft.

---

## 🧠 Approach & Design

The chatbot follows a deterministic rule-based approach:

1. **Input Preprocessing**
   - Converts input to lowercase
   - Replaces punctuation with spaces
   - Normalizes whitespace

2. **Intent Detection**
   - Matches user input against predefined keywords using **Regular Expressions (Regex)**
   - Uses **intent scoring** to determine the best match
   - Resolves conflicts using **priority-based selection**

3. **Rule-Based Responses**
   - Each intent maps to a list of possible responses
   - Responses are selected randomly for variation

4. **Contextual Memory**
   - Stores user-specific information (e.g., name)
   - Enables personalized responses within the session

5. **Fallback Handling**
   - Handles unknown inputs gracefully

---

## 🗂 Project Structure

Task1_Chatbot/
│
├── chatbot.py # Main chatbot engine
├── rules.py # Intent rules and responses
├── utils.py # Text preprocessing utilities
├── README.md
└── demo.txt


---

## ⚙️ Technologies Used

- Python 3
- Standard Python libraries only
- No machine learning or black-box NLP libraries

---

## ▶️ How to Run

1. Open terminal in the project directory
2. Run the chatbot: python chatbot.py
3. Start chatting with the bot
4. Type `exit`, `quit`, or `bye` to end the conversation

---

## 💬 Sample Interaction
You: my name is Rahul
Chatbot: Nice to meet you, Rahul!

You: what is my name
Chatbot: Your name is Rahul.

You: hello
Chatbot: Hello! How can I help you?

You: bye
Chatbot: Goodbye! Have a nice day.


---

## 📈 Key Learnings

- Rule-based chatbot design
- Intent detection using keyword pattern matching
- Conversation flow control
- Context handling without machine learning
- Writing clean, modular Python code

---

## ✅ Conclusion

This project demonstrates how a rule-based chatbot can simulate conversational behavior using deterministic logic and predefined rules. It provides a strong foundation for understanding chatbot architectures before moving to machine learning–based approaches.

---

## 👤 Author

**Bhavesh Bansod**  
CodSoft Artificial Intelligence Internship – February 2026
