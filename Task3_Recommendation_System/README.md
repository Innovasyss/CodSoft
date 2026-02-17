# Recommendation System (Python)

## CodSoft Artificial Intelligence Internship – Task 3

This project implements a **Movie Recommendation System** using Python.  
It uses **User-Based Collaborative Filtering** to suggest movies to a user based on the preferences of similar users.

---

## 📌 Project Objective

To build a simple recommendation system that:
- Analyzes user preferences (ratings).
- Identifies similar users using **Cosine Similarity**.
- Recommends items (movies) that the user has not yet seen but are likely to enjoy.

---

## 🧠 Approach & Algorithms

The system relies on **Collaborative Filtering**, specifically a memory-based approach.

### Key Concepts:

1.  **Cosine Similarity**:
    - Used to measure the similarity between two users.
    - It calculates the cosine of the angle between two rating vectors.
    - A value closer to 1 indicates high similarity (users have similar tastes), while 0 indicates no correlation.

2.  **Weighted Prediction**:
    - Instead of just copying what the most similar user liked, the system calculates a **predicted score** for each movie.
    - The score is a weighted average of ratings from all other users, where the weight is the similarity score.
    - Formula:  
      $$ \text{Score} = \frac{\sum (\text{similarity} \times \text{rating})}{\sum \text{similarity}} $$
    - This ensures that ratings from highly similar users contribute more to the recommendation than those from less similar users.

---

## 🗂 Project Structure

Task3_Recommendation_System/
│
├── main.py          # User interface and main execution loop
├── recommender.py   # Core logic (Similarity calculation & Recommendation engine)
├── data.py          # Dataset (Dictionary of users and movie ratings)
└── README.md        # Project documentation

---

## ⚙️ Technologies Used

- **Python 3**
- Standard Python libraries (`math`)
- No external machine learning libraries (implemented from scratch)

---

## ▶️ How to Run

1. Open a terminal in the project directory.
2. Run the system:
   ```bash
   python main.py
   ```
3. The system will display a list of available users.
4. Enter a username to receive movie recommendations for that user.

---

## 💬 Sample Interaction

```text
Simple Movie Recommendation System
----------------------------------

Available Users:
- Alice
- Bob
- Charlie

Enter user name from above list: Alice

Calculating similarities...
Similarity between Alice and Bob: 0.94

Recommended Movies:
- Inception
- The Matrix
```

---

## 👤 Author

**Bhavesh Bansod**  
CodSoft Artificial Intelligence Internship – February 2026