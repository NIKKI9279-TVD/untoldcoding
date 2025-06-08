def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Diagonal \
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Diagonal /
        return True
    return False

def is_full(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def tic_tac_toe():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    
    current_player = "X"
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter a number (1-9): ")

        # Validate input
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Try again.")
            continue

        # Convert move to row, col
        move = int(move) - 1
        row, col = divmod(move, 3)

        if board[row][col] in ['X', 'O']:
            print("That spot is already taken. Try another.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
