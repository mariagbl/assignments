import csv

# 	#WRITES FROM A CSV
# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['col1', 'col2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])

#     #READ FROM A CSV FILE 
#  for row in rows:
#     pprint(row)

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#open a CSV file
with open ('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow (['name', 'color'])
	#Loop through veggies"
	for vegetable in vegetables:
		#Write each veggie to a CSV
		name = vegetable ['name']
		color = vegetable ['color']
		length_of_veggie = len(name)
		
		row = [name, color, length_of_veggie]

		writer.writerow (row)