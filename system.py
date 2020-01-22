from interface import *
from time import sleep

while True:
	answer = menu([
		'See Registered People',
		'Register new Person',
		'Delete a Person',
		'Exit the System'])
	if answer == 1:
		# Option to list file contents
		print('Read file')
	elif answer == 2:
		# Option to register a new person
		header('NEW REGISTER')
		print('Registering new Person')
	elif answer == 3:
		# Option to delete a person
		print('Deleting a person')
	elif answer == 4:
		# System Exit Option
		header('Leaving the System... See you later!')
		break
	else:
		# Message if you type any wrong options
		print('\033[31mERROR! Type a valid option!\033[m')
	sleep(1)
