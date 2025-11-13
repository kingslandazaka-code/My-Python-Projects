# ultra_simple_tic_tac_toe.py

board = [" "] * 9




def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(mark):
    # Rows
    if board[0] == board[1] == board[2] == mark: return True
    if board[3] == board[4] == board[5] == mark: return True
    if board[6] == board[7] == board[8] == mark: return True
    # Columns
    if board[0] == board[3] == board[6] == mark: return True
    if board[1] == board[4] == board[7] == mark: return True
    if board[2] == board[5] == board[8] == mark: return True
    # Diagonals
    if board[0] == board[4] == board[8] == mark: return True
    if board[2] == board[4] == board[6] == mark: return True
    return False


        

turn = "X"
for _ in range(9):  # max 9 moves
    print_board()
    move = int(input(f"Player {turn}, choose (1-9): ")) - 1

    if board[move] != " ":
        print("Cell taken, try again.")
        continue

    board[move] = turn

    if check_winner(turn):
        print_board()
        print(f"Player {turn} wins!")
        break

    # Switch turns
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
else:
    print_board()
    print("It's a draw!")
