#READ VEGGIES.CSV
import csv

with open('veggies.py', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

#PRINT THE VARIABLE 'VEGETABLES'
print(vegetables)

#CONVERT TO JSON 

#SAVE 'vegetables' AS VEGETABLES.JSON 
with open('cookedveggies.json', 'w') as f:
	json.dump(vegetables, f, indent=2)