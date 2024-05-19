from car import ElectricCar

my_car = ElectricCar('nissan', 'leaf', 2024)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()
print("\n")
