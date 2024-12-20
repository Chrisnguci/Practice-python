# JSON is a string -> All the content of a text file

# note : JSON always use Double notation marks
# Json module

import json # import JSON file and conert it


file = open('friends.json','r')
file_contents = json.load(file) # readfile and turn it to dictionary

print(file_contents['Friends'][0])


# Save list as json

cars = [
		{'make': 'Ford', 'Model': 'Fiesta'},
		{'male': 'Ford', 'Model':'Focus'}
]

# Using Json.dump to save a Json file
'''
Jsondump(obj,fp) 
		obj: string,
		fb: file pointer
'''
file =open('cars.json','w' ) 
json.dump(cars,file)
file.close()


# Loads : load string -> Json string -> Dictionary
# dumps : dump string -> Turn dict to json string
incorrect_cars_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(incorrect_cars_string,) 
print(incorrect_car[0])


