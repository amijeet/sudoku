import pygame
import sys
import time

sys.setrecursionlimit(10**9)
from pygame.locals import*
pygame.init()
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
boxsize = 40
FPS = 30
fpsclock = pygame.time.Clock()
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

#faltu stuff
B = [[False for i in range(9)]for j in range(9)]
count = 0 
for i in range(9):
	for j in range(9):
		if (A[i][j] == 0):
			B[i][j] = True
			count = count+1
Si = []
Sj = []
for i in range(9):
	for j in range(9):
		if (B[i][j] == True):
			Si.append(i) 
			Sj.append(j)
length = len(Si)
counter = 0 

#checking if num can be placed at a place I, J, returns False if cannot :)
def check(I, J, num1):
	flag = True
	for x in range(9):
		if(x != I):
			if(A[x][J] == num1):
				flag = False
				break 
	for y in range(9):
		if(y != J):
			if(A[I][y] == num1):
				flag = False
				break 
	for x in range(3):
		for y in range(3):
			if( (x+(I//3)*3)!=I and (y+(J//3)*3)!=J ):
				if(A[x+(I//3)*3][y+(J//3)*3] == num1):
					flag = False
					break
	return flag

#drawing the grid lines for beautication 
def draw_grid():
	for x in range(0,360,40):
		pygame.draw.line(DIS, white, (0,x), (900,x), 1)
		pygame.draw.line(DIS, white, (x,0), (x,900), 1)
		pygame.display.flip()
		pygame.time.delay(80)
	for x in range(0,360,120):
		pygame.draw.line(DIS, white, (0,x), (900,x), 3)
		pygame.draw.line(DIS, white, (x,0), (x,900), 3)
		pygame.display.flip()
		pygame.time.delay(80)

#displays the required number on the pygame window 
def printing(A,DIS,i,j,colour):
	text = font.render(str(A[i][j]), True, colour, black)
	textRect = text.get_rect()
	textRect.center = (40*(j)+20,40*(i)+20)		
	DIS.blit(text, textRect)
	pygame.display.flip()
	pygame.time.delay(40)

#drawing the initially given numbers on the pygame screen
def initial_numbers(A):
	colour = white 
	for i in range(9):
		for j in range(9):
			if(A[i][j] != 0):
				printing(A,DIS,i,j,colour)

#trying a recursive algorithm now :(
def rec(i,num,counter):
	counter=counter+1
	if(check(Si[i],Sj[i],num)==False and num<=9):
		colour = red
		printing(A,DIS,Si[i],Sj[i],colour)
		num = num + 1
		rec(i,num,counter)
	if(num>9):
		colour = red
		for z in range(i,length):
			A[Si[z]][Sj[z]] = 0
			#printing(A,DIS,Si[z],Sj[z],colour)
		i = i-1
		rec(i,A[Si[i]][Sj[i]]+1,counter)
	if(check(Si[i],Sj[i],num)==True and num<=9):
		colour = green
		if(i!=length-1):
			colour = green
			A[Si[i]][Sj[i]] = num
			printing(A,DIS,Si[i],Sj[i],colour)
			rec(i+1,1,counter)
		else:
			A[Si[i]][Sj[i]] = num
			printing(A,DIS,Si[i],Sj[i],colour)
			pygame.display.flip()
			pygame.time.delay(5000)
			sys.exit()
			pygame.quit()

def stop():
	pygame.display.update()

#main game loop 
DIS = pygame.display.set_mode((360,360))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		else :
			draw_grid()
			initial_numbers(A)
			rec(0,1,0)
		pygame.display.update()
		fpsclock.tick(FPS)
