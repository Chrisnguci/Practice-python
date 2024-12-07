
class Student:
	def __init__(self,name,school):
		self.name = name
		self.school = school
		self.marks = []

	def avarage(self):
		return sum(self.marks)/len(self.marks)

# inheritance -> remove duplicate
class WorkingStudent(Student):
	def __init__(self,name,school,salary):
		super().__init__(name,school) #  call parrent class
		self.salary =salary
	@property # Turn no argument method into a property
	def weekly_salary(self): # Just calculate not any action(connecting database,...)
		return self.salary * 25

	
chris = WorkingStudent('Chris','PTIT',20)
print(chris.salary)
print(chris.weekly_salary)