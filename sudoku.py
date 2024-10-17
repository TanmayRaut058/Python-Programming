import random
import math

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

def fill_sudoku(gs, size):
	possible = set(range(1, size+1))
	for row in range(size):
		for col in range(size):
			available = set(gs[row] + [r[col] for r in gs])
			candidate = list(possible - available)
			n = len(candidate)-1
			gs[row][col] = candidate[random.randint(0, n)]
	return gs


def create_sudoku_puzzle(gs,num):
	l=len(gs)
	size=len(gs)**2
	required_positions=math.ceil(num*size/100)
	candidates=[]
	c=list(range(0,size))
	for _ in range(required_positions):
		p=candidates.append((random.choice(c)//l,random.choice(c)%l))

	for r,cr in candidates:
		gs[r][cr]=' '

	return gs,candidates
	


def initialize_game():
	print("-----------------Welcome to Sudoku!--------------------")
	n = int(input("Enter the grid size : "))
	board = [[' ']*n for i in range(0,n)]
	board = fill_sudoku(board, n)
	print_board(board)

	difficulty = {1: ('Very Easy', 25), 2: ('Easy', 35), 3: ('Medium', 50), 4: ('Hard', 60), 5: ('Very Hard', 75)}
	print("Difficulty Levels: ")
	for i in range(len(difficulty)):
		print(f" Level {i + 1} : {difficulty[i+1][0]}")

	level = int(input("Choose the difficulty level (1-5): "))
	
	board = create_sudoku_puzzle(board, difficulty[level][1])
	return board


def start(gs, ep):
    user_sol = [row[:] for row in gs]  # Make a copy of the grid for user input
    print_board(user_sol)
    print(f"Now you need to provide values:")
    
    for r, c in ep:  # Use the empty positions from ep
        user_sol[r][c] = int(input(f"row: {r+1} col: {c+1} ({r+1},{c+1}): "))
    
    return user_sol


def stop(gs,user_sol):
	for row in range(len(gs)):
		for col in range(len(gs)):
			if gs[row][col]!=user_sol[row][col]:
				return False
	return True



def sudoku():
	gs,ep=initialize_game()
	user_sol=start(gs,ep)
	if stop(gs,user_sol):
		print("Congrats!, you have won the match")
	else:
		print("ohhh! your guess was wrong")



sudoku()
