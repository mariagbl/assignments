import csv

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    item = dict(row) # Convert Ordered Dict to regular dict (python 3.6 or higher)
    print(item)


#Define Headers for CSV
#Write data-defined vegetables 
vegetables = [
  { "name": "eggplant", "color": "purple" },
  { "name": "tomato", "color": "red" },
  { "name": "corn", "color": "yellow" },
  { "name": "okra", "color": "green" },
  { "name": "arugula", "color": "green" },
  { "name": "broccoli", "color": "green" }
]

#Write Headers for CSV
import csv - #imported csv files

with open('testwrite.csv', 'r') as f: #opened file
    reader = csv.DictReader(f)
    rows = list(reader)

#write header
	writer= csv.writer(f)
	writerwriterow (['name', 'color'])
		
	#Loop through veggies
	for vegetable in vegetables:
    item = dict(row) # Convert Ordered Dict to regular dict (python 3.6 or higher)
    print(item)
		#Write data 
		name = vegetable ['name']
		color = vegetable ['color']
		row = [name,color]
		writer.writerow(row)
