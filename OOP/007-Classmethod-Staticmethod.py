
class Student:
	def __init__(self,name,school):
		self.name = name
		self.school = school
		self.marks = []

	def avarage(self):
		return sum(self.marks)/len(self.marks)

# classmethod
class Foo:
	@classmethod # you want have access  to the class
	def hi(cls): # class method
		print(cls.__name__)

my_foo = Foo()
my_foo.hi()


#static method
class Bar:
	@staticmethod # Use when doesn't object or class but related
	def hi():
		print("Hello, i don't take parameters")

my_bar = Bar()
my_bar.hi()