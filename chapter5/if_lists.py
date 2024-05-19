# 5-8, 5-9 Hello admin

usernames = ['jo', 'meow', 'woof', 'raja', 'admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again')
else:
    print('We need to find some users!')

# checking usernames
current_users = ['JO', 'meow', 'woof', 'Raja', 'admin']
new_users = ['RAJE', 'Meow', 'nalls', 'raja', 'ice']

# users to lowercase
existing_users = []
for current_user in current_users:
    user = current_user.lower()
    existing_users.append(user)
print(f'Exiting users in lower case: {existing_users}')

# check new users against existing usernames
for new_user in new_users:
    if new_user.lower() in existing_users:
        print(f'Username {new_user} already exists!')
    else:
        print(f'Username {new_user} is available')

