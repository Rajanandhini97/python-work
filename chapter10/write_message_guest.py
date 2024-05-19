from pathlib import Path

path = Path('guest.txt')

guest_name = input("Welcome, please enter your name: ")
path.write_text(guest_name.title())
