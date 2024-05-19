from pathlib import Path

path = Path('guest_book.txt')
guest_name = ''

while True:
    user_input = input("Please enter your firstname lastname, \n(Type 'q' to quit): ")
    if user_input == 'q':
        break
    guest_name += f"{user_input.title()}\n"

path.write_text(guest_name)