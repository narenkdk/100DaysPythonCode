#Day 82: Implement Tic-Tac-Toe


#Implement a game (e.g., Tic-Tac-Toe, Hangman) in Python.

# Tic-Tac-Toe Game in Python

# Function to print the board
def print_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw(board):
    return all([cell != " " for cell in board])

# Main function to run the game
def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get user input
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        # Make the move
        board[move] = current_player

        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
