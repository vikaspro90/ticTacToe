# Author 		: Vikas Palakurthi
# Date written 	: Dec 2015

import sys
from copy import deepcopy
def getAllPossibleMoves(board):
	#should return 1 to 9 not 0 to 8
	possibleMoves = []
	for i in range(0, len(board)):
		if board[i] == " ":
			possibleMoves.append(i+1)
	return possibleMoves

def swapPlayer(symbol):
	if symbol == 'x':
		return 'o'
	else:
		return 'x'

def miniMax(board, symbol, turn, com):
	if gameLost(com, board):
		return 0
	if gameWon(com, board):
		return 2
	possibleMoves = getAllPossibleMoves(board)
	if len(possibleMoves) > 0:
		opti = None
		for item in possibleMoves:
			newBoard = deepcopy(board)
			newBoard = updateBoard(symbol, item, newBoard)
			if turn == "max":
				value = miniMax(newBoard, swapPlayer(symbol), "min", com)
				if value >= opti:
					opti = value
			elif turn == "min":
				value = miniMax(newBoard, swapPlayer(symbol), "max", com)
				if opti == None or value <= opti:
					opti = value
	else:
		# The game is neither won nor lost, and there are no possible moves left. So it is a draw.
		opti = 1
	return opti

def makeComMove(board, symbol, turn):
	possibleMoves = getAllPossibleMoves(board)
	com = symbol
	opti = None
	for move in possibleMoves:
		newBoard = deepcopy(board)
		newBoard = updateBoard(symbol, move, newBoard)
		# updated the board with com move
		# min is the player, hence the player symbol is sent to minimax below
		value = miniMax(newBoard, swapPlayer(symbol), "min", com)
		if value >= opti or opti == None:
			opti = value
			finalChoice = move
	return finalChoice

def updateBoard(symbol, choice, board):
	board[choice-1] = symbol
	return board

def displayBoard(board):
	for i in range(0, 9):
		if (i+1)%3 == 0:
			print board[i]
		else:
			print board[i], "|",

def checkIfPossible(choice, board):
	if choice in range(1,10) and board[choice-1] == " ":
		return True
	else:
		return False

def gameWon(symbol, board):
	if (board[0] == board[1] == board[2] == symbol) or (board[3] == board[4] == board[5] == symbol) or (board[6] == board[7] == board[8] == symbol) or (board[0] == board[3] == board[6] == symbol) or (board[1] == board[4] == board[7] == symbol) or (board[2] == board[5] == board[8] == symbol) or	(board[0] == board[4] == board[8] == symbol) or	(board[2] == board[4] == board[6] == symbol):
		return True
	else:
		return False

def gameDraw(board):
	if " " in board:
		return False
	else:
		return True

def gameLost(symbol, board):
	if (board[0] == board[1] == board[2] == swapPlayer(symbol)) or (board[3] == board[4] == board[5] == swapPlayer(symbol)) or (board[6] == board[7] == board[8] == swapPlayer(symbol)) or (board[0] == board[3] == board[6] == swapPlayer(symbol)) or (board[1] == board[4] == board[7] == swapPlayer(symbol)) or (board[2] == board[5] == board[8] == swapPlayer(symbol)) or	(board[0] == board[4] == board[8] == swapPlayer(symbol)) or	(board[2] == board[4] == board[6] == swapPlayer(symbol)):
		return True
	else:
		return False

if __name__ == "__main__":
	board = 9*[" "]
	numberBoard = range(1,10,1)
	player = raw_input("What symbol would like to use X or O ?")

	if player.lower() == 'x':
		player = 'x'
		com = 'o'
	elif player.lower() == 'o':
		player = 'o'
		com = 'x'
	else:
		print "Wrong choice, aborting the game"
		sys.exit(0)

	if player =='o':
		choice = makeComMove(board, com, "max")
		board = updateBoard(com, choice, board)

	while(True):
		displayBoard(board)
		print "Please make a move by chosing a position..."
		displayBoard(numberBoard)
		choice = input("Enter choice(1 to 9): ")
		while(not checkIfPossible(choice, board)):
			choice = input("That position already taken or does not exist. Please enter a valid choice(1 to 9)")
		board = updateBoard(player, choice, board)
		if gameWon(player, board):
			displayBoard(board)
			print "You won the game.. Well played.. Congrats :)"
			sys.exit(0)
		elif gameDraw(board):
			displayBoard(board)
			print "It is a tie.. Good game :)"
			sys.exit(0)

		choice = makeComMove(board, com, "max")
		board = updateBoard(com, choice, board)

		if gameWon(com, board):
			displayBoard(board)
			print "Sorry... You lose.. better luck next time.. :)"
			sys.exit(0)
		elif gameDraw(board):
			displayBoard(board)
			print "It is a tie.. Good game :)"
			sys.exit(0)