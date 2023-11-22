
# global variables
# tictactoe Board
top_row = [' ', ' ', ' ']
middle_row = [' ', ' ', ' ']
bottom_row = [' ', ' ', ' ']
board = [top_row, middle_row, bottom_row]

# predefined methods
'''
    This is the starting function that allows player one to choose X or O
    Will assign the unchosen sign to player 2
    repeats if other symbol selection
'''
def chose_symbol():
    global player1Marker
    player1Marker = ""
    global player2Marker
    player2Marker = ""
    while player1Marker != "X" and player1Marker != "O":
        player1Marker = input("Player 1, choose X or O: ")
        if player1Marker != "X" and player1Marker != "O":
            print("Symbol does not exist, try again!")
        else:
            print("Symbol Chosen")
            if player1Marker == "X":
                player2Marker = "O"
            else:
                player2Marker = "X"
            print(f"Player 1 is: {player1Marker}\nPlayer 2 is: {player2Marker}")

'''
    prints the board for the game
'''
def print_board(board):
    for i in range(len(board)):
        str_row = "|"
        for j in range(len(board[i])):
            str_row += board[i][j]
            # str_row += 'x'
            str_row += "|"
        print(str_row)
        if i < len(board)-1:
            print("=======")  

'''
    take a user imput and put it into the array
'''
def insert_X_or_O(player, index):
    if index == 1 and bottom_row[0] == " ":
        bottom_row[0] = player
    elif index == 2 and bottom_row[1] == " ":
        bottom_row[1] = player
    elif index == 3 and bottom_row[2] == " ":
        bottom_row[2] = player
    elif index == 4 and middle_row[0] == " ":
        middle_row[0] = player
    elif index == 5 and middle_row[1] == " ":
        middle_row[1] = player
    elif index == 6 and middle_row[2] == " ":
        middle_row[2] = player
    elif index == 7 and top_row[0] == " ":
        top_row[0] = player
    elif index == 8 and top_row[1] == " ":
        top_row[1] = player
    elif index == 9 and player[2] == " ":
        top_row[2] = player
    else:
        # position not available
        return False
    return True

'''
    checks all possible combinations for end game 
    horizontal, diagnal, vertical - one player wins
    all spots filled, tie
'''
def check_if_end_game(player, board):
    if ((board[0][0] == player and board[0][1] == player and board[0][2] == player) or {board[1][0] == player and board[1][1] == player and board[1][2] == player} or (board[2][0] == player and board[2][1] == player and board[2][2] == player)):
        # horizontal check
        if player == player1Marker:
            print(f"Player 1 wins")
        elif player == player2Marker:
            print("Player 2 wins")
    elif (() or () or ()):
         # vertical check
        if player == player1Marker:
            print(f"Player 1 wins")
        elif player == player2Marker:
            print("Player 2 wins")
    elif (() or ()):
        # diagonal check
        if player == player1Marker:
            print(f"Player 1 wins")
        elif player == player2Marker:
            print("Player 2 wins")
    else:
        # none of the combination wins
        # check if all filled => game end: tie
        # check if not all filled => game not end
        for i in range(len(board)):
            for j in range(len(board[i])):
                # check if empty
                if board[i][j] == " ":
                    return False
                    # game not end
        # true = game ends
        print("Game Tie!")
        return True

    # true = game ends
    return True
    

'''
    all functions will run here
'''
# play game
def play_game():
    while(check_if_end_game() != True):
        pass
    # chose_symbol()
    # print_board(board)
    pass

play_game()


