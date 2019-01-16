import json

#read super hero json
with open('superheroes.json', 'r') as f:
    data = json.load(f)

#Loop through each member
members = superheros ['members']
for members in members:
	print(member)

#save data for each member into a csv road 

import csv

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    #header
    header =['name',	'age', 'secretIdentity', 'powers',	'squadName',	'homeTown',	'formed	secretBase',	'active']
    
    #Loop through each member
	members = superheros ['members']
		for members in members:
		row = [
			member ['name'],
			member ['age'],
			member ['secretIdentity'], 
			member ['powers'],
			superheroes ['squadName'],	
			superheroes ['homeTown'],
			superheroes	['formed'],	
			superheroes ['secretBase'],
			superheroes ['active'],
	   ] 
    writer.writerow(['val1', 'val2'])