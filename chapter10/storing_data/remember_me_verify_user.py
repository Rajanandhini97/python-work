from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    user_info = {}

    username = input("What is your name? ")
    user_info['username'] = username
    age = input("What is your age? ")
    user_info['age'] = int(age)
    city = input("Where are you located? ")
    user_info['city'] = city

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user  by name."""
    path = Path('user_info.json')
    user_info = get_stored_username(path)
    if user_info:
        print(f"Are you {user_info['username']}?")
        user_input = input("Print yes or no: ")
        if user_input == 'yes':
            print(f"{user_info['username'].title()} of age {user_info['age']} comes from {user_info['city'].title()}.")
        else:
            user_info = get_new_username(path)
            print(f"We'll remember you when you come back, {user_info['username']}")
    else:
        user_info = get_new_username(path)
        print(f"We'll remember you when you come back, {user_info['username']}")


greet_user()