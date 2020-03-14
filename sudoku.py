import sys
sys.setrecursionlimit(10**9)

#taking input 
A = [[0 for i in range(9)]for j in range(9)]
A=	[[0,0,9,0,4,0,0,0,0],
	[0,0,0,0,0,5,3,1,0],
	[0,6,1,0,0,8,0,5,0],
	[0,0,5,4,0,0,2,0,3],
	[0,1,0,0,0,7,0,0,8],
	[0,8,0,0,0,0,7,6,0],
	[3,0,6,0,1,9,4,0,0],
	[7,0,0,0,0,0,0,0,0],
	[0,0,4,0,5,0,6,2,7]]

#our B matrix which has the all the information about which box has no number in it :)
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

#trying a recursive algorithm now :(
def rec(i,num,counter):
	counter=counter+1
	if(check(Si[i],Sj[i],num)==False and num<=9):
		num = num + 1
		rec(i,num,counter)
	if(num>9):
		for z in range(i,length):
			A[Si[z]][Sj[z]] = 0
		i = i-1
		rec(i,A[Si[i]][Sj[i]]+1,counter)
	if(check(Si[i],Sj[i],num)==True and num<=9):
		if(i!=length-1):
			A[Si[i]][Sj[i]] = num
			rec(i+1,1,counter)
		else:
			A[Si[i]][Sj[i]] = num
			printmatrix()
			print("")
			print(counter)
			sys.exit()

#prints the updated matrix :)
def printmatrix() :
	for p in range(9):
		for q in range(9):
			print( A[p][q], end=" ")
		print("\n",end="")

rec(0,1,0)
