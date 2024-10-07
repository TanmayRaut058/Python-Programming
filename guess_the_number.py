import random

def guess_the_number(n):
	chances = 10
	turn = 1
	while chances > 0:
		user_input = int(input("Guess the number 1-100 : "))
		if user_input == n:
			return "Congrajulation you guessed correct on {0} turn".format(turn)
		elif user_input < n:
			print("Your guess was Low. Think Higher")
			turn += 1
			chances -= 1
		elif user_input > n:
			print("Your guess was High. Think Lower")
			turn += 1
			chances -= 1

	return "Your Chances were exhausted"


number = random.randint(1, 100)
print(guess_the_number(number))	