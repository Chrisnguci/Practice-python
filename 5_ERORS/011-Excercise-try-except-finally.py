def interact():
	while True:
		try:
			user_input = int(input("Please give me the number "))

		except ValueError:
			print(ValueError("Plese enter integers only"))
		else:
			print('{} is {}.'.format(user_input,'even' if user_input %2 ==0 else 'odd'))
		finally:
			keep= input("Do you want to play again? (y/n) ").lower()
			if keep != 'y':
				break


interact()

