from lib.interface import *
from lib.file import *
from time import sleep

arc = 'personregistration.txt'

if not file_exist(arc):
	create_file(arc)

while True:
	answer = menu([
		'See Registered People',
		'Register new Person',
		'Delete a Person',
		'Exit the System'])
	if answer == 1:
		# Option to list file contents
		read_file(arc)
	elif answer == 2:
		# Option to register a new person
		header('NEW REGISTER')
		name = str(input('Name: '))
		age = read_int('Age: ')
		register(arc, name, age)
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
