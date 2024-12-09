
class Car:
	def __init__(self,make,model):
		self.make = make
		self.model =model

	def __repr__(self):
		return f'<Car {self.make} {self.model}>'


class Garage:
	def __init__(self):
		self.cars=[]

	def __len__(self):
		return len(self.cars)

	def add_car(self,car):
		if not isinstance(car,Car): # Return True/False if the specified object is the specified  type
			raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.') # Str_class or Car_class
		self.cars.append(car)
charlies = Garage()
car=Car('Lamboghini','Urus')
charlies.add_car(car)
print(charlies.cars)