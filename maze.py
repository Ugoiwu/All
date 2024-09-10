from random import randint



#Generate the two board for the maze.
lastGoodCase = None
lastGoodCaseDir = []
size = int(input('Size of the maze ? '))
bigBoard = [["0" for _ in range(size*2+1)] for _ in range(size*2+1)]
board = [[0 for _ in range(size)] for _ in range(size)]
for i in bigBoard:
    i[0], i[-1] = "║", "║"


# Choose the first position of the board to start the generation of the maze.
startRdmPos = randint(0,size*4-3)
startPosCalc = int(str((startRdmPos/(size*4))/0.25)[0])
startPosCalc2 = startRdmPos-(startPosCalc*size)
if startPosCalc == 0:
    board[0][startPosCalc2-1] = 1
elif startPosCalc == 1:
    board[startPosCalc2][-1] = 1
elif startPosCalc == 2:
    board[-1][-1-startPosCalc2] = 1
elif startPosCalc == 3:
    board[-2-startPosCalc2][0] = 1


# Determine the first coordinates
for i, j in zip(board, range(size)):
    try:
        firstCo = [j, i.index(1)]
    except:
        pass


# Next generation of board (esthetic)
for i in bigBoard:
    for j in range(len(i)):
        i.insert(j*2, " ")
    i.remove(" ")

bigBoard[0], bigBoard[-1] = ["═" for _ in range(size * 4+1)], ["═" for _ in range(size * 4+1)]
bigBoard[0][0], bigBoard[0][-1], bigBoard[-1][0], bigBoard[-1][-1] = "╔", "╗", "╚", "╝" 


# Few functions
def showBoard(t: int):
    if t == 0:
        for i in bigBoard:
            i = map(str, i)
            print("".join(i))
    elif t == 1:
        for i in board:
            print(*i)

def checkCases(x: int, y: int):
    lGC = []
    lGCD = []
    for i,j in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        try:
            if (board[x+i][y+j]) == 0:
                lGCD.append([x+i, y+j])
        except:
            pass
    if len(lGCD) > 1:
        lGC = [x, y]
    return lGC, lGCD

showBoard(1)
print(firstCo)

# Starting generating the maze
# def genMaze(board):