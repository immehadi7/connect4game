def print_board(board):
    for row in board:
        print("-", end=" ")
        for cell in row:
            print(cell, end=" - ")
        print()

def initialize_board():
    return [[" " for _ in range(7)] for _ in range(6)]

def is_valid_move(board, row, column):
    return board[row][column] == " "

def drop_disc(board, row, column, player):
    if is_valid_move(board, row, column):
        board[row][column] = player
        return True
    return False

def is_winner(board, player):
    # Check horizontally
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertically
    for row in range(3):
        for col in range(7):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonally (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonally (top-right to bottom-left)
    for row in range(3):
        for col in range(3, 7):
            if all(board[row + i][col - i] == player for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = initialize_board()
    player = "X"

    while True:
        print_board(board)

        row = int(input(f"Player {player}, choose a row (0-5): "))
        column = int(input(f"Player {player}, choose a column (0-6): "))
        
        if 0 <= row <= 5 and 0 <= column <= 6:
            if drop_disc(board, row, column, player):
                if is_winner(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                else:
                    player = "O" if player == "X" else "X"
            else:
                print("Invalid move. The selected cell is already occupied. Please try again.")
        else:
            print("Invalid move. Please choose a valid row and column.")

if __name__ == "__main__":
    main()
