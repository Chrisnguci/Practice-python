'''Coding Exercise: Converting CSV to JSON
Write a program that reads a CSV file named csv_file.txt.

Each line in the file will contain data in the format:
club,city,country
Remove any trailing newline characters (\n) and split the line by commas.

python
Copy code
{
    'club': <club>,
    'city': <city>,
    'country': <country>
}
Append the dictionary to a list named json_list.
Write the json_list data to aFor each line:

Create a dictionary with the following structure: file named json_file.txt in JSON format. '''


import json
with open('csv_file.txt','r') as file:
    writer = file.read()
    data_rows = writer.split('\n')
    header = data_rows[0]
    main_rows =[ row for row in data_rows[1:] ] 
file.close()

headers=header.split(',')

json_list=[]


for row in main_rows:
    dict_data = {}
    for i in range(0,len(headers)):

        dict_data[headers[i]]=main_rows[i]
        json_list.append(dict_data)

json_file=open('json_file.json','w') 
json.dump(json_list,json_file)

