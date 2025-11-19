import random

def show_board(game_board): 
    """Display the current state of the board."""
    col_width = max(len(str(x)) for row in game_board for x in row)
    top = "┌" + "┬".join("─"*(col_width+2) for _ in game_board[0]) + "┐"
    middle = "├" + "┼".join("─"*(col_width+2) for _ in game_board[0]) + "┤"
    bottom = "└" + "┴".join("─"*(col_width+2) for _ in game_board[0]) + "┘"
    print(top)
    for i, row in enumerate(game_board):
        print("│ " + " │ ".join(str(x).ljust(col_width) for x in row) + " │")
        if i < len(game_board) - 1:
            print(middle)
    print(bottom)

def choice_maker(game_board, role):
    """Ask the player for a valid move and place it on the board."""
    while True:
        try:
            choice = int(input("Enter the block you want to place your move in (1-9): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if not 1 <= choice <= 9:
            print("Choose a number between 1 and 9.")
            continue

        row = (choice - 1) // 3
        col = (choice - 1) % 3

        if isinstance(game_board[row][col], str):
            print("That block is already taken. Try another.")
            continue

        game_board[row][col] = role
        return game_board

def next_move(board, robot_role):
    """Advanced move chooser algorithm"""
    for i in range(3):
        for j in range(3):
            if not isinstance(board[i][j], str):
                board[i][j] = robot_role
                return board
    return board

def check_winner(board):
    """Checks rows, columns, diagonals for a winner."""
    lines = board + [list(col) for col in zip(*board)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])
    for line in lines:
        if line.count(line[0]) == 3 and isinstance(line[0], str):
            return line[0]
    # Tie check
    if all(isinstance(cell, str) for row in board for cell in row):
        return "Tie"
    return None

def game(): 
    """Run the game."""
    roles = ["O", "X"]
    game_role = random.choice(roles)
    robot_role = "O" if game_role == "X" else "X"
    game_board = [[1,2,3],[4,5,6],[7,8,9]]
    game_status = None
    print(f"You are playing as '{game_role}'")
    if game_role == "O":
        print("Your opponent starts the game...")

    show_board(game_board)
    while game_status is None:
        # Player move
        game_board = choice_maker(game_board, game_role)
        show_board(game_board)
        game_status = check_winner(game_board)
        if game_status:
            break

        # Robot move
        print("Robot's turn:")
        game_board = next_move(game_board, robot_role)
        show_board(game_board)
        game_status = check_winner(game_board)

    if game_status == "Tie":
        print("It's a tie!")
    else:
        print(f"The winner is: {game_status}")

game()
