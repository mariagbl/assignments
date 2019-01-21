# filter blacklist veggie names
import json

#read file 
with open('veggies2.json', 'r') as f:
	#f reading it as text
	#use json library and parse it into json 
	veggies = json.load(f)
	print(veggies)

#generate final list you will add to. Array 1) Green 2) All finding green
green_veggies = []
blacklist = ['arugula', 'broccoli', 'okra']
#for row(can call this anything) in data source:
#have to define variable in loop  
for types in veggies:
	if type['name'] not in blacklist:
		green_veggies.append(row)

		print(green_veggies)