 friends =  
   {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter to age < 37
millenials = []
for friend in friends:
    if row['age'] < 37:
        millenials.append(row)

print(millenials)