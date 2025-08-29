import math

def print_board(board):
    print("\n    0   1   2")
    print("  +---+---+---+")
    for i, row in enumerate(board):
        print(f"{i} | " + " | ".join(row) + " |")
        print("  +---+---+---+")
    print()

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if is_full(board): return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human, ai = "X", "O"

    print("Welcome to Tic-Tac-Toe! You are 'X' and AI is 'O'.")
    print_board(board)

    while True:
        # validated human input
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid range! Please enter numbers 0, 1, or 2.")
                    continue
                if board[row][col] != " ":
                    print("Cell already taken, choose another.")
                    continue
                board[row][col] = human
                break
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        print_board(board)
        if check_winner(board) == human:
            print(" You wOn Broo!")
            return
        if is_full(board):
            print("Dang it's a draw!")
            return

        print("AI is making a move...")
        best_move(board)
        print_board(board)

        if check_winner(board) == ai:
            print(" AI wins! Better luck next time.")
            return
        if is_full(board):
            print("It's a draw!")
            return
play_game()
