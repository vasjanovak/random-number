# say hello to user and ask him to tell you his name
print('Welcome to the game of Guessing the number.')
player_name = input('Please tell me your name: ')


def game():
	# import function for random number
	from random import randint

	# set highest number
	highest = 2

	# set range
	number = randint(1, highest)

	# number of tries
	tries = 0

	# ask him to set highest number
	highest = int(input('Please enter highest number {}: '.format(player_name)))

	# ask him to guess the random number
	current_num = int(input("Guess the number between 1-{0} {1}: ".format(highest, player_name)))

	# check the number
	while current_num != number:
		if current_num > number:
			print("Aim lower {}".format(player_name))
			current_num = int(input("Try smaller number: "))
		elif current_num < number:
			print("Aim higher {}".format(player_name))
			current_num = int(input("Try higher number: "))
		tries += 1  # number of tries

	else:
		print("You guessed it {}".format(player_name))
		print("You needed {} tries".format(tries))
		play_again = input("Would you like to play again {}? y/n".format(player_name))
		if play_again == 'y':
			game()


# start the game
game()
