class Restaurant:
    """Simple info about the restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe restaurant"""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        """Tells if the restaurant is open or not"""
        print(f"Restaurant {self.restaurant_name} is now open.")

    def set_number_served(self, customer_count):
        """Set the value for number of customers served"""
        self.number_served = customer_count

    def increment_number_served(self, increment_count):
        """Increment the count of number of customers served"""
        self.number_served += increment_count
        print(f"Number of customers served today: {self.number_served}")
