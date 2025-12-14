import math

# Initialize empty board
board = [" " for _ in range(9)]

# Print the board
def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

# Check if a player has won
def check_winner(player):
    winning_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check for draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

# AI move using minimax
def ai_move():
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

# Main game loop
def play_game():
    print("===== TIC TAC TOE AI =====")
    print("You are X | AI is O")
    print("Enter numbers between 0 and 8 as shown below:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8")

    print_board()

    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except:
            print("Please enter a valid number.")
            continue

        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("congratulations, great move You win!")
            break

        if is_draw():
            print_board()
            print("sorry, It's a draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("oops, AI wins!")
            break

        print_board()

# Run the game
play_game()
