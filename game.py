
# global variables
# tictactoe Board
top_row = [' ', ' ', ' ']
middle_row = [' ', ' ', ' ']
bottom_row = [' ', ' ', ' ']
board = [top_row, middle_row, bottom_row]

# predefined methods
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

def insert_X_or_O():
    pass

# play game
def play_game():
    chose_symbol()
    # print_board(board)
    pass

play_game()


