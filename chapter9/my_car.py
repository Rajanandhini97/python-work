from car import Car
from electric_car import ElectricCar

my_car = Car('audi', 'a4', '2020')
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.update_odometer(30)
my_car.read_odometer()
print("\n")

my_used_car = Car('subaru', 'outback', '2015')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23400)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_mustang = ElectricCar('nissan', 'leaf', 2024)
print(my_mustang.get_descriptive_name())