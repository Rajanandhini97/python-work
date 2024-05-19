guests = ['meow', 'woof', 'koo']

#initial invite
for guest in guests:
    print(f"Hi {guest.title()}, you should join us for dinner today")
print("\n")

#removing guests that declined invite
invite_declined_by = guests.pop()
print(f"{invite_declined_by.title()} won't be able to make it\n")

#inviting new guest
guests.append('moo')
for guest in guests:
    print(f"Hi {guest.title()}, you should join us for dinner today")
print("\n")

#bigger table
print("We found a bigger table and hence would like to invite more people")

guests.insert(0, 'rakshu')
guests.insert(2, 'maha')
guests.append('bharath')

#updated list for bigger room

for guest in guests:
    print(f"Hi {guest.title()}, you should join us for dinner tonight")
print("\n")

#Shrinking list
print("Hello all, sorry we can only have two guests over tonight\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry :( {removed_guest.title()}, we don't have enough seating for the dinner today")
print("\n")

for guest in guests:
    print(f"Welcome aboard {guest.title()} !!")
print("\n")

#emptying list

del guests[0:2]
print(guests)
