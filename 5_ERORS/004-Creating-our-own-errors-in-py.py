
class MyCustomError(TypeError):
	"""
Custom Error with message and specified code include TypeError class
	"""
	def __init__(self,message,code):
		super().__init__(f'Error code {code}: {message}' )
		self.code = code


answer =int(input())
if answer < 0: 
	err = MyCustomError("Choose the positive number",500)
	print(err.__doc__) # Test the doc
# 1. Message include
# Ex "200","Success" -> Message + code
# 2. multiline string -< uderneath class, function -> become docs string