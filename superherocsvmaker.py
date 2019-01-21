#import json
#import csv

#read superheroes.json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

#print(superheroes) 

#write a csv with rows per member 

#Loop through each member
members = superheroes ['members']
for members in members:
	print(member)

#save data for each member into a csv road 
with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	#header
	headers =['name', 'age', 'secretIdentity', 'powers',	'squadName',	'homeTown',	'formed	secretBase',	'active']
	
	#write header 
	writer.writerow(headers)

	#write members into csv file 
	#for superhero in superheroes:
		#print(superheroes)

	#define members
	members = superheroes ['members']

	#Loop through each member
	for members in members:
			#alternate format: 
			#name = member['name']
			#age = member['age']
			#squadName = superheroes['secretBase']
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
	firstpower = member ['powers'][0]
#write data to csv files 

# Should be enabled: 
# row = [
#list all vairables
#add first power after all headers as continued list "age, firstpower"
#]

write.writerow(rows)