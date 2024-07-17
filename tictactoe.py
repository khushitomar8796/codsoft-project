import math
import random

# Constants
X = 'X'  # Human player
O = 'O'  # AI player
EMPTY = ' '

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('-------------')

# Function to check if a player has won
def check_win(player, board):
    lines = (
        # rows
        board,
        # columns
        zip(*board),
        # diagonals
        [[board[i][i] for i in range(3)]],
        [[board[i][2 - i] for i in range(3)]]
    )
    return any(all(cell == player for cell in line) for line in lines)

# Function to check if the current board state is a terminal state (win/draw)
def is_terminal_state(board):
    return check_win(X, board) or check_win(O, board) or all(all(cell != EMPTY for cell in row) for row in board)

# Function to evaluate the current board state
def evaluate(board):
    if check_win(O, board):
        return 1
    elif check_win(X, board):
        return -1
    else:
        return 0

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if is_terminal_state(board):
        return evaluate(board)

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to get the best move using Minimax with Alpha-Beta Pruning
def get_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = O
                eval = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = X if random.choice([True, False]) else O  # Randomly choose starting player

    while not is_terminal_state(board):
        print_board(board)

        if current_player == X:
            row, col = map(int, input("Enter your move (row[1-3] col[1-3]): ").split())
            row -= 1  # convert to 0-based index
            col -= 1  # convert to 0-based index
            if board[row][col] == EMPTY:
                board[row][col] = X
                current_player = O
            else:
                print("Invalid move. Try again.")
                continue
        else:
            row, col = get_best_move(board)
            board[row][col] = O
            current_player = X

    print_board(board)
    result = evaluate(board)
    if result == 1:
        print("AI wins!")
    elif result == -1:
        print("You win!")
    else:
        print("It's a draw!")

# Start the game
if __name__ == "__main__":
    play_game()