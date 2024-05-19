# 7-1
car_name = input("What kind of car would you like to rent ?: ")
print(f"Let me see if I can find you a {car_name.title()}")

# 7-2
guests_no = input("How many guests for dinning ?: ")
guests_no = int(guests_no)

if guests_no > 8:
    print("Sorry, please wait while we find a table for you")
else:
    print("Great, we have a table ready for you")

# 7-3
user_number = int(input("Please enter an integer, and I will tell you if it's div by 10: "))

if user_number % 10 == 0:
    print(f"{user_number} is a multiple of 10")
else:
    print(f"{user_number} is not a multiple of 10")