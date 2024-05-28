from random import randrange

board = ("--------------------")
mark = "x"
position = 3

def move(board, mark, position):
    # Returns the game board with the given mark in the given position.

    return board[:position-1] + mark + board[position:]

def player_move(board):
    mark = "x"
    while True:
        position = int(input("In which position (1-20) do you want to place your mark? Position = "))
    
        if position < 1:
            print("The position has to be between 1 and 20.")
        elif position > 20:
            print("The position has to be between 1 and 20.")
        elif board[position-1] != "-":
            print("This position is already occupied. Select another position.")
        else:
            break
        
    return move(board, mark, position)

def pc_move(board):
    mark = "o"

    while True:
        position = randrange(1, 21)
        if board[position-1] == "-":
            break
                
    return move(board, mark, position)

def evaluate(board):
    if "xxx" in board:
        game_state = "x"  # X has won
    elif "ooo" in board:
        game_state = "o"  # o has won
    elif "-" not in board:
        game_state = "!"  # nobody won, draw
    else:
        game_state = "-"  # game is not finished

    return game_state

def oneD_tictactoe():
    board = ("--------------------")

    while evaluate(board) == "-":
        board = player_move(board)
        print(board)
        board =  pc_move(board)
        print(board)

    return "The winner is : " + evaluate(board)

print(oneD_tictactoe())
