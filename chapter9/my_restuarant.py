from restaurant import Restaurant

restaurant_one = Restaurant('Copper kitchen', 'indo-chinese')
# print(new_restaurant.restaurant_name)
# print(new_restaurant.cuisine_type.title())

restaurant_one.describe_restaurant()

restaurant_two = Restaurant('Al-ajwain', 'lebanese')
restaurant_two.describe_restaurant()
print(f"Number of customers served: {restaurant_two.number_served}")

restaurant_two.number_served = 3
print(f"Number of customers served: {restaurant_two.number_served}")

restaurant_two.set_number_served(6)
print(f"Number of customers served: {restaurant_two.number_served}")
restaurant_two.increment_number_served(5)
print(f"Number of customers served: {restaurant_two.number_served}")