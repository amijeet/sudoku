import pygame, sys, time, random
from pygame.locals import*
pygame.init()

W = 452
DIS = pygame.display.set_mode((W, W))
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font = pygame.font.Font('freesansbold.ttf',25)

#A MATRIX
A =	[[5,0,1,6,9,0,0,7,0],
	[0,0,4,7,0,5,3,0,8],
	[0,6,7,0,0,8,0,1,5],
	[0,3,5,4,0,1,0,2,0],
	[6,0,0,3,5,7,1,8,0],
	[1,4,0,0,0,0,7,5,0],
	[0,5,0,0,6,0,2,0,7],
	[2,0,6,0,3,4,5,0,1],
	[4,1,0,0,7,0,0,3,6]]

#main algo
def solveSudoku(A, row, col):
    if row == 8 and col == 9:
        # printNumbers(row, col, GREEN)
        return True
    
    if col == 9:
        row += 1
        col = 0

    if A[row][col] > 0:
        # printNumbers(row, col, GREEN)
        return solveSudoku(A, row, col+1)
    
    for num in range(1, 10 ):
        if check( row, col, num):
            A[row][col] = num
            printNumbers(row, col, GREEN)
            if solveSudoku(A, row,col+1):
                return True
        A[row][col] = 0
        printNumbers(row, col, RED)
    return False

#checking if num can be placed at a place I, J, returns False if cannot :)
def check(I, J, num1):
	for x in range(9):
		if(x != I):
			if(A[x][J] == num1):
				return False 
	for y in range(9):
		if(y != J):
			if(A[I][y] == num1):
				return False
	for x in range(3):
		for y in range(3):
			if( (x+(I//3)*3)!=I and (y+(J//3)*3)!=J ):
				if(A[x+(I//3)*3][y+(J//3)*3] == num1):
					return False
	return True

# prints any number given to it
def printNumbers( i, j, colour ):
    cellWidth = W//9
    text = font.render(str(A[i][j]), True, colour, BLACK)
    textRect = text.get_rect()
    textRect.center = (cellWidth*(j)+cellWidth/2,cellWidth*(i)+cellWidth/2)
    DIS.blit(text, textRect)
    pygame.display.flip()
    time.sleep(10/1000)

# print initial numbers
def initialNumbers( A ):
    for i in range(9):
        for j in range(9):
            if A[i][j] is not 0:
                printNumbers(i, j, WHITE)

# draws the grid!
def drawGrid():
    for x in range(0, 452, W//9 ):
        pygame.draw.line( DIS, WHITE, (x, 0), (x, W) )
        pygame.draw.line( DIS, WHITE, (0, x), (W, x) )
    for x in range(0, 452, W//3 ):
        pygame.draw.line( DIS, BLUE, (x, 0), (x, W) )
        pygame.draw.line( DIS, BLUE, (0, x), (W, x) )

# the main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    drawGrid()
    initialNumbers(A)
    solveSudoku( A, 0, 0 )
    pygame.display.update()