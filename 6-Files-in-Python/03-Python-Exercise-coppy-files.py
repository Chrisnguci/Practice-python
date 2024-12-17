# Ask the user for a list of 3 friends
# For each friend , we'll tell the user whether the are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

#hint: readlines() -> if user in the people -> put them into nearby_friends

import os
nearby_file = os.path.join(os.getcwd(),'nearby_friends.txt')
people_file= os.path.join(os.getcwd(),'people.txt')

user_input = input("Enter 3 Fiends: ")
try:
	friends= user_input.split(" ")
except Exception as e:
	raise e
else:
	if len(friends) !=3:
		raise ValueError("Plese Enter 3 Friends")



friends_set = set(friends)
with open(people_file,'r') as file:
	nearby_people= file.readlines()
file.close()

# List comprehension 
nearby_people = [friend.strip() for friend in nearby_people]
people_nearby_set = set(nearby_people) 
print(people_nearby_set)
# using intersection
nearby_friends_set = friends_set.intersection(people_nearby_set)

with open(nearby_file,'w') as file : 
	for friend in nearby_friends_set:
			file.write(f"{friend}\n")

file.close()

