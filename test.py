import csv

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    #write header
    writer.writerow(['col1', 'col2'])

    #define data
    data= []
   		 (['val1', 'val2'])
    		(['val1', 'val2'])
   		(['val1', 'val2'])

    #write data
    for row in rows:
    	writer.writerow(row)

import csv

#READ CSV

with open('testwrite.csv', 'r') as f:
    reader = csv.DictReader(f) #object you have to define
    rows = list(reader) #takes dict reader and puts it into the array of dictionaries

for row in rows:
    item = dict(row) # Convert Ordered Dict to regular dict (python 3.6 or higher)
    print(item)