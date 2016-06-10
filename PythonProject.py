import random

def drawBoard(board):
    print('     |     |     |     |     ')
    print('  ' + board[21] + '  |  ' + board[22] + '  |  ' + board[23] + '  |  ' + board[24] + '  |  ' + board[25])
    print('     |     |     |     |     ')
    print('-----------------------------')
    print('     |     |     |     |     ')
    print('  ' + board[16] + '  |  ' + board[17] + '  |  ' + board[18] + '  |  ' + board[19] + '  |  ' + board[20])
    print('     |     |     |     |     ')
    print('-----------------------------')
    print('     |     |     |     |     ')
    print('  ' + board[11] + '  |  ' + board[12] + '  |  ' + board[13] + '  |  ' + board[14] + '  |  ' + board[15])
    print('     |     |     |     |     ')
    print('-----------------------------')
    print('     |     |     |     |     ')
    print('  ' + board[6] + '  |  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + '  |  ' + board[10])
    print('     |     |     |     |     ')
    print('-----------------------------')
    print('     |     |     |     |     ')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + '  |  ' + board[4] + '  |  ' + board[5])
    print('     |     |     |     |     ')

# Chose the letter
def playerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def firstMove():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'you'

def playAgain():
    print('Play Again? (y/n)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    winner = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],
              [1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24],[5,10,15,20,15],
              [1,7,13,19,25],[6,9,13,17,21]]

    for i in range(len(winner)):
        for j in range(len(winner[0])):
            if bo[winner[i][0]] == le and bo[winner[i][1]] == le and bo[winner[i][2]] == le and bo[winner[i][3]] == le and bo[winner[i][4]] == le:
                return True



def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def playerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split() or not isSpaceFree(board, int(move)):
        print('Your Turn (1-25)')
        move = input()
    return int(move)

def randomMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def compMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Check if the next move is a winner
    for i in range(1, 26):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the next player move is the winner
    for i in range(1, 26):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Take corners and middle of the sides
    move = randomMove(board, [1, 3, 5, 6, 10, 11, 15, 16, 20, 21, 23, 25])
    if move != None:
        return move

    # Take center
    if isSpaceFree(board, 13):
        return 13

    # All of the other spaces
    return randomMove(board, [2, 4, 6, 7, 8, 9, 12, 14, 16, 17, 18, 19, 20, 22, 24])

def isBoardFull(board):
    for i in range(1, 26):
        if isSpaceFree(board, i):
            return False
    return True



while True:
    theBoard = [' '] * 26
    playerLetter, computerLetter = playerLetter()
    turn = firstMove()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        # Player's turn
        if turn == 'you':
            drawBoard(theBoard)
            move = playerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You Won')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Tie')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn
            move = compMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You Lose')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Tie')
                    break
                else:
                    turn = 'you'

    if not playAgain():
        break