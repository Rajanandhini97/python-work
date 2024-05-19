# 5-1

pizza = 'pepperoni'
print("Is it pepperoni ?")
print(pizza == 'pepperoni')

print("Is it margherita ?")
print(pizza == 'margherita')

car = 'BMW'
print("Is it BMW ?")
print(car == 'bmw')

print("Is it BMW ?")
print(car.lower() == 'bmw')

score_1 = 20
score_2 = 23

print(f"Score check {score_1 > 21 and score_2 > 21}")
print(f"Score check {score_1 > 21 or score_2 >= 21}")


pizzas = ['spicy paneer', 'cheese corn', 'chicken', 'margherita', 'pepperoni', 'veg kurma', 'chipotle chicken']
print(f"Have anything in paneer ? {'spicy paneer' in pizzas}")
print(f"Have anything in pork ? {'pork' in pizzas}")