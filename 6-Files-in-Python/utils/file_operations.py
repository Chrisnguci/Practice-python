

# Use the context manager to open the file and write the content
def save_to_file(content,filename):
	with open(filename,'w') as file:
		file.write(content)


# Using context manager to open the file read and return a string
def read_file(filename):
	with open(filename) as file:
		return file.read()



