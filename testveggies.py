#read veggies csv file
import csv
import json

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f) #converts to json type format
    rows = list(reader)

#prints rows
#print(json.dumps(rows,indent=2))#could use this to print nicely
#pprint(rows) #could use this too


#for row in rows:
    #item = dict(row) # Convert Ordered Dict to regular dict (python 3.6 or higher)
    #print(item)


#WRITE JSON TO A FILE 

with open('vegetables.json', 'w') as f:
    json.dump(rows, f, indent=2)
