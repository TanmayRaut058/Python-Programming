import random

def print_board(board):
	n = len(board)
	for i in range(0,n):
		print('-'.center(4*n+1, '-'))
		for j in range(0, n):
			if j == 0:
				print("| {0} | ".format(board[i][j]), end = '')
			else :
				print("{0} | ".format(board[i][j]), end = '')
		print()
	print('-'.center(4*n+1, '-'))

	return 0

def play_game(board):
	turn = random.randint(0,1)
	n = len(board)*len(board)
	counter = 0

	while counter < n:
		if turn == 0:
			print_board(board)
			if turn == 0:
				print("Player 1's Turn (X)")
				x = int(input("P1 Enter x coordinate: "))
				y = int(input("P1 Enter y coordinate: "))
				if board[x][y] == ' ':
					board[x][y] = 'X'
					turn = 1
					counter += 1
				else:
					print("This spot is already taken. Try again.")
					continue
		elif turn == 1:
			print_board(board)
			if turn == 1:
				print("Player 2's Turn (O)")
				x = int(input("P2 Enter x coordinate : "))
				y = int(input("P2 Enter y coordinate : "))
				if board[x][y] ==' ':
					board[x][y] = 'O'
					turn = 0
					counter += 1
				else:
					print("This spot is already taken. Try again.")
					continue
		
		if counter > (n+n):
			winner = check_winner(board)
			if winner is not None:
				print_board(board)
				print("Player {0} wins!".format('1' if winner == 'X' else '2'))
				return 0
		

	print_board(board)
	print("It's a draw!")
	
	return 0		

def check_winner(board):
	n = len(board)
    
	for row in board:
		if row.count(row[0]) == n and row[0] != ' ':
			return row[0]
		
	for col in range(n):
		column = [board[row][col] for row in range(n)]
		if column.count(column[0]) == n and column[0] != ' ':
			return column[0]
		
	if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(n)):
		return board[0][0]
	

	if all(board[i][n - 1 - i] == board[0][n - 1] and board[i][n - 1 - i] != ' ' for i in range(n)):
		return board[0][n - 1]
	
	return None

def initialize_game():
	n = int(input("Enter the grid size : "))
	board = [[' ']*n for i in range(0,n)]
	play_game(board)
	return None

initialize_game()
