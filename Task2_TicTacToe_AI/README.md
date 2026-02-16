# Tic-Tac-Toe AI (Python)

## CodSoft Artificial Intelligence Internship – Task 2

This project implements an unbeatable **Tic-Tac-Toe AI** using Python.  
The AI plays against a human player and uses the **Minimax algorithm with Alpha-Beta Pruning** to determine the optimal move, ensuring it never loses.

---

## 📌 Project Objective

To implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player.  
The goal is to make the AI **unbeatable** using game theory algorithms.

---

## 🧠 Approach & Algorithms

The AI uses the **Minimax Algorithm**, a recursive decision-making algorithm used in game theory for two-player zero-sum games.

### Key Features:
1.  **Minimax Algorithm**:
    - The AI simulates all possible future moves to determine the best outcome.
    - It assumes the human player also plays optimally.
    
2.  **Alpha-Beta Pruning**:
    - Optimizes the Minimax algorithm by "pruning" (ignoring) branches in the game tree that don't need to be evaluated.
    - This significantly improves performance and speed.

3.  **Depth-Based Scoring**:
    - The AI prefers winning sooner rather than later.
    - It also tries to prolong the game if a loss is inevitable (though in Tic-Tac-Toe, it never loses).

---

## 🗂 Project Structure

Task2_TicTacToe_AI/
│
├── main.py       # Main game loop and user interface
├── game.py       # Tic-Tac-Toe board logic and rules
├── minimax.py    # AI algorithm (Minimax + Alpha-Beta Pruning)
└── README.md     # Project documentation

---

## ⚙️ Technologies Used

- **Python 3**
- Standard Python libraries only (no external dependencies)

---

## ▶️ How to Run

1. Open a terminal in the project directory.
2. Run the game:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to play.
   - You play as **X**.
   - The AI plays as **O**.
   - Enter a number (0-8) to place your mark on the board.

---

## 💬 Sample Interaction

```text
Welcome to Tic-Tac-Toe (Human vs AI)
You are X, AI is O

Board Positions:
0 | 1 | 2
--+---+--
3 | 4 | 5
...
AI wins!
```

---

## 👤 Author

**Bhavesh Bansod**  
CodSoft Artificial Intelligence Internship – February 2026