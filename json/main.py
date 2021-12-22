import json

persons = [
    {'name': "Kojo", 'age': 23},
    {'name': "AMa", 'age': 20},
    {'name': "Hamida", 'age': 20},
    {'name': "Jonior", 'age': 12},
    {'name': "Coded", 'age': 24},
    {'name': "Mohammed", 'age': 13},
    {'name': "Ayisha", 'age': 28},
    {'name': "Elder", 'age': 30},
    {'name': "Ali", 'age': 30},
    {'name': "Nimatu", 'age': 30},
]

personJson = json.dumps(persons, skipkeys=True, indent=5)
print(personJson)

with open("person.json", 'w') as file:
    json.dump(persons, file, indent= 5)