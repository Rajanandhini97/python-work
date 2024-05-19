class Employee:
    """Stores employee name and annual salary"""

    def __init__(self, firstname, lastname, salary):
        """Initialise employee name and annual salary"""
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def give_raise(self, raise_amt=50000):
        """Add bonus amount to annual salary"""
        self.salary += raise_amt