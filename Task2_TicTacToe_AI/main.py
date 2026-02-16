from game import TicTacToe
from minimax import get_best_move


def print_position_guide():
    print("Board Positions:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8\n")


def main():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe (Human vs AI)")
    print("You are X, AI is O\n")

    print_position_guide()

    while True:
        # Human move
        try:
            position = int(input("Enter your move (0-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        if position not in range(9):
            print("Position must be between 0 and 8.")
            continue

        if not game.make_move(position, "X"):
            print("Position already taken. Try again.")
            continue

        game.print_board()
        print()

        # Check if human wins
        if game.check_winner("X"):
            print("You win!")
            break

        if game.is_draw():
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = get_best_move(game)
        game.make_move(ai_move, "O")

        game.print_board()
        print()

        # Check if AI wins
        if game.check_winner("O"):
            print("AI wins!")
            break

        if game.is_draw():
            print("It's a draw!")
            break                               


if __name__ == "__main__":
    main()
