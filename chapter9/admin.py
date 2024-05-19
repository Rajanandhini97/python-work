from user import User


class Privileges:
    """Describes available privileges for a user"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Displays available privileges for a user"""
        print("\nUser has the following privileges")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Prints info about admin a special type of user"""

    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes of the parent class
        Then initialize attributes specific to an electric car"""
        super().__init__(first_name, last_name, age, location)
        self.privilege = Privileges()
