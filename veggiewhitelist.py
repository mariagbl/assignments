# filter whitelist  veggie names
import json

#read file 
with open('veggies2.json', 'r') as f:
	#f reading it as text
	#use json library and parse it into json 
	veggies = json.load(f)
	print(veggies)

#generate final list you will add to. Array 1) Green 2) All finding green
green_veggies = []
whitelist = ['arugula', 'broccoli', 'okra']
#for row(can call this anything) in data source:
#have to define variable in loop  
for row in veggies:
	if row['name'] in whitelist:
		print(row['name'])
		green_veggies.append(row)

print(json.dumps(green_veggies, indent=2))

#write to json files
with open ('greenveggies.json', 'w') as f:
		json.dumps(green_veggies,indent=2)

#write to csv
with open ('greenveggies.json', 'w') as f:
	writer=csv.writer(f)
	writer.writerow(['name','color'])
	for veggie in greenveggies:
		name= veggie['name']
		color =veggie['color']
		writer.writerow([name,color])