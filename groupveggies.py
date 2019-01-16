
#worked with classmate from design school to check a couple of pieces of code
#read veggies.csv
from pprint import pprint

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]
#group by color

veggies_by_color = {}
for vegetable in vegetables:
	#assigning variable, color for whatever vegetable in
    color = vegetable['color']
    #if we have color with name in empty dict lets refer to it and add
    if color in veggies_by_color:
        veggies_by_color[color].append(vegetable)
	#otherwise lets create an entry for it   
    else:
        veggies_by_color[color] = [vegetable]

pprint(veggies_by_color)
#print to terminal

#output to JSON file 