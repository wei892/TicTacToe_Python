def playGame():
    choseSymbol()

playGame()

def choseSymbol():
    player1Marker = ""
    player2Marker = ""

    while player1Marker != "X" and player1Marker != "O":
        player1Marker = input("Player 1, choose X or O: ")
        print(player1Marker)
        print(player1Marker == "X")
        if player1Marker != "X" and player1Marker != "O":
            print("Symbol does not exist, try again!")
        else:
            print("Symbol Chosen")

def printBoard():
    pass



