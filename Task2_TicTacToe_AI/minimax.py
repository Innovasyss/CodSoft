def minimax(game, depth, is_maximizing, alpha, beta):
    """
    Recursive Minimax algorithm with Alpha-Beta Pruning.
    Returns the best score for the current board state.
    """

    # Terminal state checks
    if game.check_winner("O"):  # AI wins
        return 10 - depth
    elif game.check_winner("X"):  # Human wins
        return depth - 10
    elif game.is_draw():  # Draw
        return 0

    # Maximizing player (AI)
    if is_maximizing:
        best_score = float("-inf")

        for move in game.available_moves():
            game.make_move(move, "O")
            score = minimax(game, depth + 1, False, alpha, beta)
            game.undo_move(move)

            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break

        return best_score

    # Minimizing player (Human)
    else:
        best_score = float("inf")

        for move in game.available_moves():
            game.make_move(move, "X")
            score = minimax(game, depth + 1, True, alpha, beta)
            game.undo_move(move)

            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break

        return best_score


def get_best_move(game):
    """
    Returns the optimal move for AI.
    """
    best_score = float("-inf")
    best_move = None

    for move in game.available_moves():
        game.make_move(move, "O")
        score = minimax(game, 0, False, float("-inf"), float("inf"))
        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
