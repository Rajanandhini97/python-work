# Start with users that need to be verified, and an empty list to hold confirmed users.

unconfirmed_users = ['nandhini', 'karen', 'jarvis']
confirmed_users = []

# loop to verify and add unconfirmed users to confirmed list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())