def power_of_two():
	user_input = input('Please enter a number: ')
	try:
		n = float(user_input)

	except ValueError:
		print('Your input was invalid. Using default value 0')
		n=0

	else: # if n is string the else will not be execute
		n_square = n**2
		return n_square



def else_pw_two():
	user_input= input('Please enter a number ')
	try:
		n = float(user_input)
	except ValueError :
		print("Input Invalid, using default value 0")
		return 0.0
	else:
		n_square = n**2
		return n_square


print(else_pw_two())