def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(board) * 4 - 1))


def check_winner(board, size, win_cond, player):
    # Check rows
    for row in board:
        if "".join(row).find(player * win_cond) != -1:
            return True
    
    # Check columns
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if "".join(column).find(player * win_cond) != -1:
            return True
    
    # Check diagonals
    for r in range(size - win_cond + 1):
        for c in range(size - win_cond + 1):
            # Check diagonal from top-left to bottom-right
            if all(board[r + i][c + i] == player for i in range(win_cond)):
                return True
            # Check diagonal from top-right to bottom-left
            if all(board[r + i][c + win_cond - 1 - i] == player for i in range(win_cond)):
                return True

    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe(size=3, win_cond=3):
    board = [[" " for _ in range(size)] for _ in range(size)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter your move row (0-{size - 1}): "))
        col = int(input(f"Player {players[current_player]}, enter your move column (0-{size - 1}): "))

        if board[row][col] != " ":
            print("This cell is already occupied. Try again.")
            continue

        board[row][col] = players[current_player]

        if check_winner(board, size, win_cond, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = 1 - current_player


if __name__ == "__main__":
	board_size = int(input("Enter the board size: "))
	win_condition = int(input("Enter the winning condition (how many in a row needed to win): "))
	tic_tac_toe(board_size, win_condition)
