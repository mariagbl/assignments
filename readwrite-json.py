import json

#rREADING A JSON FILE
with open('superheroes.json', 'r') as f:
    data = json.load(f)

pprint(data)

#WRITING A JSON FILE

rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('testwrite.json', 'w') as f:
    json.dump(rows, f, indent=2)