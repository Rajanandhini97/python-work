# # 6-7
# person_0 = {
#     'first_name': 'nandhini',
#     'last_name': 'nallusamy',
#     'age': '26',
#     'city': 'toronto',
# }
#
# person_1 = {
#     'first_name': 'aish',
#     'last_name': 'nallusamy',
#     'age': '23',
#     'city': 'chennai',
# }
#
# person_2 = {
#     'first_name': 'raje',
#     'last_name': 'nallusamy',
#     'age': '49',
#     'city': 'dindigul',
# }
#
# people = [person_0, person_1, person_2]
#
# for person in people:
#     full_name = f"{person['first_name']} {person['last_name']}"
#     print(f"{full_name.title()} of age {person['age']} lives in {person['city'].title()}")

# # 6-8
# pet_0 = {
#     'name': 'rio',
#     'breed': 'german shepard',
#     'age': '1',
# }
#
# pet_1 = {
#     'name': 'marley',
#     'breed': 'golden retriever',
#     'age': '6',
# }
#
# pet_2 = {
#     'name': 'eric',
#     'breed': 'beagle',
#     'age': '3',
# }
#
# pets = [pet_0, pet_1, pet_2]
#
# for pet in pets:
#     if int(pet['age']) <= 1:
#         print(f"{pet['name'].title()} is a {pet['breed']} and is {pet['age']} year old")
#     else:
#         print(f"{pet['name'].title()} is a {pet['breed']} and is {pet['age']} years old")

# # 6-9
# fav_places = {
#     'aish': ['chennai'],
#     'nan': ['toronto', 'montreal', 'chennai'],
#     'raje': ['chennai', 'dindigul'],
#     'maha': ['kerala', 'chennai'],
# }
#
# for name, places in fav_places.items():
#     if len(places) <= 1:
#         print(f"\n{name.title()}'s favourite place is:")
#         print(places[0].title())
#     else:
#         print(f"\n{name.title()}'s favourite places are:")
#         for place in places:
#             print(place.title())

# # 6-10
# fav_num = {
#     'raja': [6, 5, 10],
#     'aish': [5, 7, 9, 3],
#     'ma': [8, 1, 2],
#     'nalls': [10, 4],
# }
#
# for name, nums in fav_num.items():
#     print(f"\n{name.title()}'s fav numbers are {nums}")

# 6-11
cities = {
    'chennai': {
        'country': 'india',
        'population': '6,599,000',
        'fact': 'Gateway to South India',
    },
    'toronto': {
        'country': 'canada',
        'population': ' 2,794,356',
        'fact': 'Toronto is a multicultural city',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()} is in {info['country'].title()} with a population of {info['population']}")
    print(f"Fun fact: {info['fact']}")

cities['montreal'] = {
    'country': 'canada',
    'population': '3,000,000',
    'fact': 'best food'
}

print(f"New dictionary: {cities['montreal']}")