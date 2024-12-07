
class Student:
	def __init__(self,name):
		self.name = name

#dunder method

class  Garage:
	def __init__(self):
		self.cars=[]

	def __len__(self):
		return len(self.cars)

	def __getitem__(self,index): # access the index of a list
		return self.cars[index]
	def get_index(self,index):
		return self.cars[index]

	def __repr__(self): # Print out string represent the object -> For programmer, Appear when debuggr
		return f'<Garage {self.cars}>'

	def __str__(self): # Return a string tell the user information about this Garage -> For user
		return f'Grage with {len(self)} cars'
ford=Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford[1])# __getitem__
print(ford.get_index(1)) 
print(ford) # call str or str