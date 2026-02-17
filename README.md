# CodSoft Artificial Intelligence Internship

## 👨‍💻 Author: Bhavesh Bansod
**Domain:** Artificial Intelligence  
**Batch:** February 2026

---

## 📌 Overview

This repository contains the solutions for the three tasks completed during the **CodSoft Artificial Intelligence Internship**. These projects demonstrate fundamental AI concepts, ranging from rule-based logic and game theory to collaborative filtering algorithms, implemented purely in Python without external machine learning libraries.

---

## 📂 Projects

### 1️⃣ Task 1: Rule-Based Chatbot
An advanced conversational bot that understands user intent using pattern matching and predefined rules.

- **Objective:** Build a chatbot that responds to user queries based on specific rules and context.
- **Key Algorithms:**
  - **Regex & Pattern Matching:** Identifies keywords in user input.
  - **Intent Scoring:** Calculates the best matching rule based on keyword density and priority.
  - **Context Awareness:** Remembers user details (e.g., name) during the session.
- **Location:** `Task1_Chatbot/`

### 2️⃣ Task 2: Tic-Tac-Toe AI
An unbeatable AI agent that plays Tic-Tac-Toe against a human player.

- **Objective:** Implement an AI that plays optimally and never loses.
- **Key Algorithms:**
  - **Minimax Algorithm:** A recursive algorithm that evaluates all possible future moves to find the optimal strategy.
  - **Alpha-Beta Pruning:** Optimizes the search tree by eliminating branches that don't need to be evaluated, improving performance.
- **Location:** `Task2_TicTacToe_AI/`

### 3️⃣ Task 3: Recommendation System
A movie recommendation engine using collaborative filtering.

- **Objective:** Suggest movies to users based on the preferences of similar users.
- **Key Algorithms:**
  - **User-Based Collaborative Filtering:** Finds users with similar rating histories.
  - **Cosine Similarity:** Mathematically measures the similarity between user preference vectors.
  - **Weighted Prediction:** Scores unseen movies based on a weighted average of similar users' ratings.
- **Location:** `Task3_Recommendation_System/`

---

## ⚙️ Technologies Used

- **Language:** Python 3.x
- **Libraries:** Standard Python libraries only (`math`, `re`, `random`, `copy`)
- **Philosophy:** No "black box" ML libraries; all algorithms are implemented from scratch to demonstrate core understanding.

---

## ▶️ How to Run

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd CodSoft
   ```

2. **Run Task 1 (Chatbot):**
   ```bash
   cd Task1_Chatbot
   python chatbot.py
   ```

3. **Run Task 2 (Tic-Tac-Toe):**
   ```bash
   cd Task2_TicTacToe_AI
   python main.py
   ```

4. **Run Task 3 (Recommendation System):**
   ```bash
   cd Task3_Recommendation_System
   python main.py
   ```

---

## 📜 License

This project is created for educational purposes as part of the CodSoft Internship.