def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        print(f"Hello, {name.title()}")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)