import csv



movies = [
	{"name": "The Matrix","director": "Wachowski"},
	{"name": "Green Book","director": "Farrelly"},
	{"name": "Amadeus", "director": "Forman"}
	
]
def write_to_file(output):
	with open('file.csv','w') as f:
		writer = csv.DictWriter(f,fieldnames=list(output[0].keys())) # much easier than maunual
		writer.writeheader()
		writer.writerows(output) # accept of a list of Dict
		#f.write("name,director\n")
		#writer.writerows([elem.values() for elem in output])
		

#write_to_file(movies)


def read_from_file():
	with open('file.csv','r') as f:
		reader = csv.DictReader(f) # create a reader object
		for line in reader:
			print(line['name'],line['director'])


read_from_file()

'''
Instead of manually writing and reading, use
- csv.writer and csv.reader
- csv.DictWriter and csv.DictReader help you with named datat
- The csv module also takes care of formating edge cases, like commas in your strings
* writerows : write a list of dict
* writerow : write a dict
* csv.DictReader -> object 


'''
