board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]


# prints the board
def printBoard(turns):
    print("Turn: " + str(turns))
    print("  0 1 2")
    for i in range(3):
        print(str(i) + " " + board[i][0] + " " + board[i][1] + " " + board[i][2])
    print()


# takes a mark and puts it in the row and col inputted
def putMarkHelper(mark, row, col):
    board[row][col] = mark


# makes all values blank
def clearBoard():
    for i in range(3):
        for j in range(3):
            board[i][j] = "-"


# asks for input for col and row, checks if valid too
def putMark():
    global turn
    global x
    try:
        column = int(input(getPlayer() + ", what column do you want to leave a mark in? "))
        rows = int(input(getPlayer() + ", what row do you want to leave a mark in? "))
    except ValueError:
        print("Enter a number from 0 - 2.")
        putMark()
    if column < 3 and rows < 3 and board[rows][column] == "-":
        if turn % 2 == 0:
            putMarkHelper("X", rows, column)
        else:
            putMarkHelper("O", rows, column)
    else:
        print("Not a valid spot, try again.")
        putMark()
    turn = turn + 1


# checks if someone won by row
def checkRow():
    global x
    global turn
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != "-":
            turn = turn - 1
            print(getPlayer() + " wins!")
            x = (input("Continue playing? ")).upper()
            if x == "YES":
                clearBoard()
                turn = 0


# checks if someone won by column
def checkColumn():
    global x
    global turn
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "-":
            turn = turn - 1
            print(getPlayer() + " wins!")
            x = (input("Continue playing? ")).upper()
            if x == "YES":
                clearBoard()
                turn = 0


# checks if someone won by diagonal
def checkDiagonal():
    global x
    global turn
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "-":
        turn = turn - 1
        print(getPlayer() + " wins!")
        x = (input("Continue playing? ")).upper()
        if x == "YES":
            clearBoard()
            turn = 0
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[0][2] != "-":
        turn = turn - 1
        print(getPlayer() + " wins!")
        turn = turn + 1
        x = (input("Continue playing? ")).upper()
        if x == "YES":
            clearBoard()
            turn = 0


# checks if someone won
def checkWinner():
    checkDiagonal()
    checkColumn()
    checkRow()


# returns which player is allowed to make a move for the current turn
def getPlayer():
    if turn % 2 == 0:
        return "Player 1"
    else:
        return "Player 2"


# checks if tie
def checkTie():
    global turn
    global x
    if turn == 9:
        print("Tie")
        x = (input("Continue playing? ")).upper()
        if x == "YES":
            clearBoard()
            turn = 0


# allows user to exit the game if value is not equal to "YES"
x = "YES"
turn = 0
while x == "YES":
    printBoard(turn)
    putMark()
    checkWinner()
    checkTie()

print("Thanks for playing!")
