# 6-1
person = {
    'first_name': 'Nandhini',
    'last_name': 'Nallusamy',
    'age': '26',
    'city': 'chennai',
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'].title())
print("\n")

# 6-2
fav_num = {
    'raja': 6,
    'aish': 5,
    'ma': 8,
    'nalls': 10
}

for k, v in fav_num.items():
    print(f'{k} fav number is {v}')
print("\n")

# 6-3
glossary = {
    'function': 'small code block of useful logic',
    'method': 'function of a class',
    'dictionary': 'stores key value pairs',
    'lists': 'collection of items in a particular order',
    'variables': 'represent data in your program',
}

for k, v in glossary.items():
    print(f"{k} : {v}")