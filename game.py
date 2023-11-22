
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
    if index not in range(1, 10):
        return False
    
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
def check_if_end_game(player):
    if (
        (board[0][0] == player and board[0][1] == player and board[0][2] == player) 
        or 
        (board[1][0] == player and board[1][1] == player and board[1][2] == player)
        or 
        (board[2][0] == player and board[2][1] == player and board[2][2] == player)):
        print("Won horizontal")
        if player == player1Marker:
            print(f"Player 1 wins")
        elif player == player2Marker:
            print("Player 2 wins")
    elif (
        (board[0][0] == player and board[1][0] == player and board[2][0] == player) 
        or 
        (board[0][1] == player and board[1][1] == player and board[2][1] == player) 
        or 
        (board[0][2] == player and board[1][2] == player and board[2][2] == player)):
         # vertical check
        if player == player1Marker:
            print(f"Player 1 wins")
        elif player == player2Marker:
            print("Player 2 wins")
    elif (
        (board[0][0] == player and board[1][1] == player and board[2][2] == player) 
        or 
        (board[0][2] == player and board[1][1] == player and board[2][0] == player)):
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
                    print(board[i][j])
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
    print("Wecome to Tic Tac Toe!")
    # let player pick a symbol
    chose_symbol()

    # displays an empty board
    print("\n")
    print_board(board)
    print("\n"*3)

    # starts game with player one
    player1Turn = True
    player = player1Marker

    # while game is not ended, play
    while(check_if_end_game(player) != True):

        # toggling between players
        if player1Turn:
            player = player1Marker
            while True:
                try:
                    position = int(input("Player 1 turn! Make a move: "))
                except:
                    position = int("Move must be an int: ")
                else:
                    break
        else:
            player = player2Marker
            while True:
                try:
                    position = int(input("Player 2 turn! Make a move: "))
                except:
                    position = int("Move must be an int: ")
                else:
                    break

        # try making the move
        move_possible = insert_X_or_O(player, position)
        # if move doesnt work: input error and ask player to try again
        while move_possible == False:
            position = int(input("Move not possible! Try again: "))
            move_possible = insert_X_or_O(player, position)
        # # if it works, print board:
        print_board(board)
        if check_if_end_game(player) == True:
            print("Game Ended!")
            break

        # set player to other
        player1Turn = not player1Turn


play_game = True
while play_game:
    play_game()

    play_again = input("Play again? Y or N: ")
    if play_again == "Y":
        play_game = True
    else: 
        play_game = False
        break


