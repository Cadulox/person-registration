from interface import *
from time import sleep

while True:
	answer = int(input('Enter the desired option: '))
	if answer == 1:
		# Option to list file contents
		print(answer)
	elif answer == 2:
		# Option to register a new person
		header('NEW REGISTER')
		print(answer)
	elif answer == 3:
		# Option to delete a person
		print(answer)
	elif answer == 4:
		# System Exit Option
		print(answer)
		break
	else:
		# Message if you type any wrong options
		print(answer)
	sleep(1)
