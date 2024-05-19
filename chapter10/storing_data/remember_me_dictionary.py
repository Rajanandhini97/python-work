from pathlib import Path
import json


def user_info():
    """Prints user info if exists"""
    path = Path('user_info_dict.json')
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        print(f"{user_info['username'].title()} of age {user_info['age']} comes from {user_info['city'].title()}.")
    else:
        user_info = {}

        username = input("What is your name? ")
        user_info['username'] = username
        age = input("What is your age? ")
        user_info['age'] = int(age)
        city = input("Where are you located? ")
        user_info['city'] = city

        contents = json.dumps(user_info)
        path.write_text(contents)

        print(f"We'll remember you when you come back, {username}")


user_info()