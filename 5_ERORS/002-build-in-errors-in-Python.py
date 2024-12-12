# These types of error happened when you access that didn't exist in the wrong way
#IndexError
#KeyError
#NameError
#AttributError -> Fairly related 
#NotImplementedError 
#RuntimeError
#SytaxError
#IndextationError
#TabError  -> spaces or tab
#TypeError  -> Give wrong type
#ValueError
#ImportError
#DeprecationWarning 

#1.IndexError -> Access the index did not exist or incorrect
#2. Keyerror -> the key does not exist in a dictionary
#3. NameError -> Variable is not defined
#4. AttributError: Dealing with object -> Object doens't have this attribute
#5. NotImplementedError -> Point that we haven't do with this
#5. RunTimeError: A base error, base class, Others extend this one to be Runtime Errors
#6. Syntaxerror: When Mess up with python
class User # leak ':' -> SyntaxError
	def __init__(self,username,password):
		self.username=username
		self.password=password
#7. IndextationError
def add_two(x,y):
pass

#8. TabError -> spaces or tab

#9.TypeError
print(5+'hi') # TypeError: int + str( Type of the data )

#10. ValueError: 
int('20.5') #-> number not string
# note : Normally only built in function will raise a Value Error 
#11. ImportError: 
#12. DeprecationWarning : Something wrong happened -> Program will crash -> Deprecate: No longer bestway of doing something
#