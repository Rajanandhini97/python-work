#sorting lists

places = ['vancouver', 'tokyo', 'jasper', 'swiss', 'chennai']
print("Original list:", places)

#sorted()
print("Sorted method:", sorted(places))
print("Original order retained: ", places)

#reverse()
places.reverse()
print("\nReversed list", places)
places.reverse()
print("Reversing again to original list:", places)

#sort()
places.sort()
print("\nSort original list:", places)
places.sort(reverse=True)
print("Sort reverse alphabetical of sort list:", places)