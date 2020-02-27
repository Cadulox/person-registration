from lib.interface import *


def file_exist(name):
	try:
		file = open(name, 'rt')
		file.close()
	except FileNotFoundError:
		return False
	else:
		return True


def create_file(name):
	try:
		file = open(name, 'wt+')
		file.close()
	except:
		print('There was an ERROR creating the file!')
	else:
		print(f'{name} file successfully created!')


def read_file(name):
	try:
		file = open(name, 'rt', encoding='utf-8')
	except:
		print('ERROR reading the file!')
	else:
		header('REGISTERED PEOPLE')
		for line in file:
			data = line.split(';')
			data[1] = data[1].replace('\n', '')
			print(f'{data[0]:<30}{data[1]:>3} years')
	finally:
		file.close()


def register(arc, name='unknow', age=0):
	try:
		file = open(arc, 'at', encoding='utf-8')
	except:
		print('There was an ERROR opening the file!')
	else:
		try:
			file.write(f'{name};{age}\n')
		except:
			print('There was an ERROR writing the data!')
		else:
			print(f'New {name} record added')
			file.close()
