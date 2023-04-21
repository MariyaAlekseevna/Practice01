import functions

while True:
	answer = input("Command ('loc', 'zip', 'dist', 'end') => ").lower()
	if answer == 'end':
		print('Done')
		break
	elif answer == 'loc':
		functions.loc()
	elif answer == 'zip':
		functions.zip()
	elif answer == 'dist':
		functions.dist()
	else:
		print('Invalid command, ignoring')
