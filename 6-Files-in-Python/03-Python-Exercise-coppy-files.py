# Ask the user for a list of 3 friends
# For each friend , we'll tell the user whether the are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

#hint: readlines() -> if user in the people -> put them into nearby_friends

import os
friends = []

user_input = input("Enter 3 Fiends: ")
try:
	friends= user_input.split(" ")
except Exception as e:
	raise e
else:
	if len(friends) !=3:
		raise ValueError("Plese Enter 3 Friends")

nearby_file = os.path.join(os.getcwd(),'nearby_friends.txt')
people_file= os.path.join(os.getcwd(),'people.txt')
with open(people_file,'r') as file:
	current_friends= file.readlines()
file.close()
current_friends = [ friend.strip() for friend in current_friends]

for friend in friends:
	if friend in current_friends:
		print(friend)
	else:
		print(f"{friend} is not exists")

