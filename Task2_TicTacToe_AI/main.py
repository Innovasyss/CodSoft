import tkinter as tk
from tkinter import messagebox
from game import TicTacToe
from minimax import get_best_move

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        
        self.human_score = 0
        self.ai_score = 0

        self.game = TicTacToe()
        self.buttons = []
        
        self.score_label = tk.Label(self.root, text="Human: 0 - AI: 0", font=("Arial", 14))
        self.score_label.grid(row=0, column=0, columnspan=3)

        self.create_board()

    def create_board(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i+1, column=j)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def on_click(self, row, col):
        index = row * 3 + col
        
        # Human move
        if self.game.board[index] == " ":
            self.game.make_move(index, "X")
            self.update_buttons()
            
            if self.check_game_over("X"):
                return

            # AI move (small delay for better UX)
            self.root.after(500, self.ai_turn)

    def ai_turn(self):
        move = get_best_move(self.game)
        if move is not None:
            self.game.make_move(move, "O")
            self.update_buttons()
            self.check_game_over("O")

    def update_buttons(self):
        for i in range(9):
            r, c = divmod(i, 3)
            self.buttons[r][c].config(text=self.game.board[i])

    def check_game_over(self, player):
        if self.game.check_winner(player):
            if player == "X":
                self.human_score += 1
                winner = "You"
            else:
                self.ai_score += 1
                winner = "AI"
            self.score_label.config(text=f"Human: {self.human_score} - AI: {self.ai_score}")
            messagebox.showinfo("Game Over", f"{winner} won!")
            self.reset_game()
            return True
        elif self.game.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        self.game = TicTacToe()
        self.update_buttons()

def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
