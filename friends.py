#reads json and converts to a csv file
import json

#Open the file and put data in a variable
with open('friends.json', 'r') as f:
    friends = json.load(f)

#print    
#print(data)

#write to a CSV file
import csv

with open('friends.csv', 'w') as f:
    writer = csv.writer(f)

    #Write header
    writer.writerow(['name', 'age'])

    #Identify each piece of data tryng to write and define variable
    for friend in friends:
    	#{'name' : 'Rachel', 'age' : 34}
    	name = friend['name']
    	age = friend ['age']
    	writer.writerow ([name,age])
