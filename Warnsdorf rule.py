import pygame, sys, random
from pygame.locals import *
from sys import exit

def create_chessboard():
	chess = [[0]*8 for i in range(8)]
	return chess

def print_chessboard(chess_to_print):
	print("My ChessBoard:")
	for x in range (0, len(chess_to_print)):
		print(chess_to_print[x])
	
def count_onward_moves(myChess, row, col): #I use this function to count how many onward moves I can do
	possibleMoves = 0

	if (row+2 < 8 and col+1 < 8 and myChess[row+2][col+1] == 0) : #bottom-right 0
		possibleMoves += 1
	if (row+2 < 8 and col-1 > -1 and myChess[row+2][col-1] == 0): #bottom-left 1
		possibleMoves += 1
	if (row-2 > -1 and col-1 > -1  and myChess[row-2][col-1] == 0): #top-left 2
		possibleMoves += 1
	if (row-2 > -1 and col+1 < 8 and myChess[row-2][col+1] == 0): #top-right 3
		possibleMoves += 1
	if (row+1 < 8 and col+2 < 8 and myChess[row+1][col+2] == 0): #right-bottom 4
		possibleMoves += 1
	if (row-1 > -1 and col+2 < 8 and myChess[row-1][col+2] == 0): #right-top 5
		possibleMoves += 1
	if (row+1 < 8 and col-2 > -1 and myChess[row+1][col-2] == 0): #left-bottom 6
		possibleMoves += 1
	if (row-1 > -1 and col-2 > -1 and myChess[row-1][col-2] == 0):  #left-top 7
		possibleMoves += 1
	return possibleMoves

def onward_moves(myChess,row,col):
	possible_moves = ["","","","","","","",""]
	onward_moves_num = [0,0,0,0,0,0,0,0]#used to save how many onward moves I can do from the next step.
	
	if (row+2 < 8 and col+1 < 8 and myChess[row+2][col+1] == 0): #bottom-right 0
		possible_moves[0] = "br"
		onward_moves_num[0] = count_onward_moves(myChess, row+2, col+1)
		
	if (row+2 < 8 and col-1 > -1 and myChess[row+2][col-1] == 0): #bottom-left 1
		possible_moves[1] = "bl"
		onward_moves_num[1] = count_onward_moves(myChess, row+2, col-1)
		
	if (row-2 > -1 and col-1 > -1  and myChess[row-2][col-1] == 0): #top-left 2
		possible_moves[2] = "tl"
		onward_moves_num[2] = count_onward_moves(myChess, row-2, col-1)
		
	if (row-2 > -1 and col+1 < 8 and myChess[row-2][col+1] == 0): #top-right 3
		possible_moves[3] = "tr"
		onward_moves_num[3] = count_onward_moves(myChess, row-2, col+1)
		
	if (row+1 < 8 and col+2 < 8 and myChess[row+1][col+2] == 0): #right-bottom 4
		possible_moves[4] = "rb"
		onward_moves_num[4] = count_onward_moves(myChess, row+1, col+2)
		
	if (row-1 > -1 and col+2 < 8 and myChess[row-1][col+2] == 0): #right-top 5
		possible_moves[5] = "rt"
		onward_moves_num[5] = count_onward_moves(myChess, row-1, col+2)
		
	if (row+1 < 8 and col-2 > -1 and myChess[row+1][col-2] == 0): #left-bottom 6 
		possible_moves[6] = "lb"
		onward_moves_num[6] = count_onward_moves(myChess, row+1, col-2)
		
	if (row-1 > -1 and col-2 > -1 and myChess[row-1][col-2] == 0): #left-top 7
		possible_moves[7] = "lt"
		onward_moves_num[7] = count_onward_moves(myChess, row-1, col-2)
		
	#print("\nPosition in which you can move: " ,possible_moves) #print possible moves
	#print ("Number of possible moves: ", onward_moves_num)
	
	min_value = [9,9] #need this list of 2 items to save which onward_move is the best to follow.
	for i in range(0, len(onward_moves_num)): #understanding which path is smaller to follow.
		if onward_moves_num[i] < min_value[0] and onward_moves_num[i] != 0:
			min_value[0] = onward_moves_num[i]
			min_value[1] = i
	#print("Value and index of next move: ", min_value)
	
	#Returning different position depending on which square I have to move on.
	if min_value[1] == 0:
		return row+2, col+1
	elif min_value[1] == 1:
		return row+2, col-1
	elif min_value[1] == 2:
		return row-2, col-1
	elif min_value[1] == 3:
		return row-2, col+1
	elif min_value[1] == 4:
		return row+1, col+2
	elif min_value[1] == 5:
		return row-1, col+2
	elif min_value[1] == 6: 
		return row+1, col-2
	elif min_value[1] == 7:
		return row-1, col-2
	elif min_value[1] == 9: #so it didn't find any other option. This happens when I have last number to append.
		for x in range(0,8):
			for y in range(0,8):
				if myChess[x][y] == 0:
					return x, y

def knight_tour(chess,startingRow,startingColumn, i):	
	if i < 64:
		chess[startingRow][startingColumn] = i
		nextRow, nextColumn = 0, 0
		nextRow, nextColumn = onward_moves(chess,startingRow,startingColumn) #calling onward_moves
		#print("Next indexes to use: ", nextRow, nextColumn)
		if i == 63:
			chess[nextRow][nextColumn] = 64
		else:
			knight_tour(chess,nextRow,nextColumn, i+1) #recursivity

RED = (255,0,0) #just colors
BLACK = (0,0,0)
YELLOW = (255,255,0)

chessboard = []
chessboard.extend(create_chessboard()) #creating my chessboard

#CHANGE VALUES HERE TO TRY THE STARTING POINT OF THE PROGRAM.
knight_tour(chessboard, 5,5, 1)#i'm calling function passing from where the program has to start
print_chessboard(chessboard) #print result.
	

pygame.init()
surface = pygame.display.set_mode((800,800))
surface.fill(RED)
pygame.display.set_caption('KNIGHT TOUR PROBLEM')

while True:
	for _ in range(0,800,100): #draw grid
		pygame.draw.line(surface,BLACK,(_,0),(_,800),4)
		pygame.draw.line(surface,BLACK,(0,_),(800,_),4)
		
	for cont in range(1,64):
		for x in range(0,8):
			for y in range(0,8):
				if chessboard[x][y] == cont:
					for z in range(0,8):
						for q in range(0,8):
							if chessboard[x][y] == cont and chessboard[z][q] == cont+1: 
								pygame.draw.line(surface,YELLOW,(50+y*100, 50+x*100),(50+q*100, 50+z*100),3) #the line
								pygame.draw.rect(surface,YELLOW,(50+q*100, 50+z*100, 5,5),10) # the dot
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.quit()
	pygame.display.update()
	
