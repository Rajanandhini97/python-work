# slicing lists 4-10

pizzas = ['spicy paneer', 'cheese corn', 'chicken', 'margherita', 'pepperoni', 'veg kurma', 'chipotle chicken']

print(f'The first three items in the list are: {pizzas[:3]}')
print(f'Three items from the middle of the list: {pizzas[3:6]}')
print(f'The last three items in the list are: {pizzas[-3:]}')

# my pizzas your pizzas
your_pizzas = pizzas[:]

pizzas.append('mexican')
your_pizzas.append('fiesta')

print('My fav pizzas')
for pizza in pizzas:
    print(pizza)

print('\nYour fav pizzas are: ')
for pizza in your_pizzas:
    print(pizza)
