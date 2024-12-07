class FixedFloat:
	def __init__(self,amount):
		self.amount = amount

	def __repr__(self):
		return f'<FixFloat {self.amount:.2f}>' #2f : 2 decimal places
 
	@staticmethod
	def from_sum(value1,value2):
		return FixedFloat(value1+value2)
	@classmethod
	def from_sub(cls,value1,value2):
		return cls(value1+value2)

number = FixedFloat.from_sum(1.2323,2.11)
print(number)


class Euro(FixedFloat):
	def __init__(self,amount):
		super().__init__(amount)
		self.symbol = '€'

	def __repr__(self):
		return f'Euro {self.symbol}{self.amount:.2f}'

money = Euro(18.786)
print(money)
sub = FixedFloat.from_sub(1,2)
sub = sub.from_sub(4,5) # take the object from the original sub
print(sub)