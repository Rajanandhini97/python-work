class User:
    """Summarizes user information"""

    def __init__(self, first_name, last_name, age, location):
        """Initialise user name and other attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Describe's the user info"""
        print(f"{self.first_name} {self.last_name} is {self.age} years old and is from {self.location}.")

    def greet_user(self):
        """Greets the user"""
        print(f"Hi {self.first_name} {self.last_name}, welcome aboard!!")

    def increment_login_attempts(self):
        """Increment login attempt count every time when this method is called"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempt count to 0 every time when this method is called"""
        self.login_attempts = 0


# user_1 = User('Nandhini', 'Nallusamy', 26, 'Chennai')
# user_1.describe_user()
# user_1.greet_user()
# print("\n")


