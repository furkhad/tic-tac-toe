import random

def display_board(board):
    print("\n" + "\n---------\n".join([" | ".join(row) for row in board]) + "\n")

def check_winner(board, mark):
    return any(all(cell == mark for cell in row) for row in board) or \
           any(all(row[i] == mark for row in board) for i in range(3)) or \
           all(board[i][i] == mark for i in range(3)) or \
           all(board[i][2-i] == mark for i in range(3))

def is_full(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def position_to_coords(pos):
    return (pos - 1) // 3, (pos - 1) % 3

def make_move(board, mark, opponent=None):
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                board[i][j] = mark
                if check_winner(board, mark) or not opponent:
                    return True
                board[i][j] = str(3 * i + j + 1)
    return False

def ai_move(board):
    if not make_move(board, "O", "X"):
        available = [str(3 * i + j + 1) for i in range(3) for j in range(3) if board[i][j] not in ["X", "O"]]
        i, j = position_to_coords(int(random.choice(available)))
        board[i][j] = "O"

def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            i, j = position_to_coords(move)
            if board[i][j] not in ["X", "O"]:
                board[i][j] = "X"
                break
            print("Cell already occupied, try again.")
        except (ValueError, IndexError):
            print("Invalid input, try again.")

def tic_tac_toe():
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    display_board(board)
    while True:
        user_move(board)
        display_board(board)
        if check_winner(board, "X"):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        ai_move(board)
        display_board(board)
        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
