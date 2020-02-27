def line(size=42):
	return '-' * size


def header(txt):
	print(line())
	print(txt.center(42))
	print(line())


def read_int(msg):
	while True:
		try:
			number = int(input(msg))
		except (ValueError, TypeError):
			print('\033[31mERROR! Please a valid option!\033[m')
			continue
		except KeyboardInterrupt:
			print('\n\033[31mThe user preferred not to typing any options.\033[m')
			return 0
		else:
			return number


def menu(list_name):
	header('MAIN MENU')
	counter = 1
	for item in list_name:
		print(f'\033[33m{counter}\033[m - \033[34m{item}\033[m')
		counter += 1
	print(line())
	option = read_int('\033[32m Your Option: \033[m')
	return option
