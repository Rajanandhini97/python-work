"""A set of classes that can be used to represent electric cars."""

from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """Upgrades battery capacity"""
        if self.battery_size != 65:
            self.battery_size = 65
            print(f"Upgrading battery size to {self.battery_size}")
        elif self.battery_size == 65:
            print("Battery does not require upgrade")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class
        Then initialize attributes specific to an electric car"""

        super().__init__(make, model, year)
        self.battery = Battery()


my_car = ElectricCar('nissan', 'leaf', 2024)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()
print("\n")

my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()
