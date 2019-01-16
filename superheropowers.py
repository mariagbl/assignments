#load libraries
import json

#read superheros.json- reading a json file
with open('superheroes.json', 'r') as f:
   superheroes = json.load(f)

#print(members)

#create an empty array called powers
all_powers =[]

#loop through members of squad and append powers of each to the power array.
#loop through each member 
#get the members
members = superheroes ['members']
for member in members:
	#for each member get a list of the powers
	powers = member ['powers']
	print(powers)

	#loop through the powers and print each one 
	for power in powers:
		data.append(power)
		#or print(power)

#print(data)

#make the list unique 
unique_powers = list(set(all_powers))
print(unique_powers)

#print(list(set(all_powers))) #set turns into list, list turns everything into list.


