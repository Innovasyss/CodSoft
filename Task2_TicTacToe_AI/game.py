class TicTacToe:
    def __init__(self):
        # Initialize empty board
        self.board = [" " for _ in range(9)]
        self.win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

    def print_board(self):
        """Display current board state"""
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("--+---+--")

    def available_moves(self):
        """Return list of empty positions"""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        """Place a move on the board"""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def undo_move(self, position):
        """Undo a move (used in Minimax backtracking)"""
        self.board[position] = " "

    def check_winner(self, player):
        """Check if given player has won"""
        for condition in self.win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def is_draw(self):
        """Check if the game is a draw"""
        return " " not in self.board
