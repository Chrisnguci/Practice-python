
#1. Explain
try:
	x = int(input(""))
	print(x+1)
except ValueError as e: # Just catch the same Exception -> If not it will not be print out =))) ao ma vch
	print("Wrong format")

# 2. If Except : Different type error

try:
	x = int(input(""))
	print(x+1)
except ValueError as e: # Except: Catch the Error
	print("Wrong format")


# -> When that error happens different the error we want to catch -> Can't catch -> Raise the type of errors

# -> don't want the user see the Errors ->Catch errors-> help user understand the error basically 

#3. Catch multi Errors:
try:
	
	print('x'+1)
except ValueError as e: # Except: Catch the Error
	print("Wrong value")
except TypeError:
	print('Wrong Type')

#4. Finnally -> run wether or not Error happened
try:
	print('x'+1)
except ValueError as e: # Except: Catch the Error
	print("Wrong value")
except TypeError:
	print('Wrong Type')
finally:
	print('Good moring')