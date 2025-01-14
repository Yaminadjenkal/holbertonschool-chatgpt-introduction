def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.
    
    Parameters:
        board (list of list): 2D list representing the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the Tic-Tac-Toe board.
    
    Parameters:
        board (list of list): 2D list representing the Tic-Tac-Toe board.
    
    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks if the game has ended in a draw (board is full and no winner).
    
    Parameters:
        board (list of list): 2D list representing the Tic-Tac-Toe board.
    
    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # If there's an empty cell, no draw yet
    return True  # If no empty cells, it's a draw

def tic_tac_toe():
    """
    Runs the main game loop for Tic-Tac-Toe.
    Alternates turns between players X and O, displays the board, 
    and checks for a winner after each move.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize a 3x3 board with empty spaces.
    player = "X"  # Player X starts the game.
    
    while True:  # Keep playing until there is a winner or draw.
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Check if the input is valid and within bounds
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid row or column. Please enter values between 0 and 2.")
                continue  # Skip the rest of the loop and ask for input again
                
            # Check if the chosen spot is empty
            if board[row][col] == " ":
                board[row][col] = player
                # Check if there's a winner or a draw
                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                if check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                # Switch players after each valid move
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid row and column between 0 and 2.")

tic_tac_toe()

