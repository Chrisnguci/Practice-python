import os

# get the absolute file path
dir=os.path.abspath(os.getcwd())
file_name=os.path.join(dir,'data.txt')



# Reading mode
with open(file_name,'r') as file:
	data = file.read()
	print(data)
file.close()
 
# Writing mode -> overwrite data in the file -> Create new if file doesn't exist
user_input= input("Type something: ")
with open(file_name,'w') as file:	
	file.write(user_input)
file.close()
