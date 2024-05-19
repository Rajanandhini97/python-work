# # 7-4
# message = ""
#
# while message != "quit":
#     message = input(f"Enter the toppings that you want on your pizza: ")
#
#     if message == "quit":
#         break
#     else:
#         print(f"{message.title()} will be added to your pizza")

# # 7-5
# active = True
#
# prompt = "\nEnter your age to know the ticket price"
# prompt += "\nEnter 'exit' to exit the page: "
# while active:
#     user_age = input(prompt)
#
#     if user_age == 'exit':
#         active = False
#     elif int(user_age) < 3:
#         print("Free for ages under 3")
#     elif int(user_age) <= 12:
#         print("Ticket cost is $10")
#     else:
#         print("Ticket cost is $15")

# 7-6
prompt = "\nEnter your age to know the ticket price"
prompt += "\nEnter 'exit' to exit the page: "

user_age = ""

while user_age != 'exit':
    user_age = input(prompt)

    if user_age == 'exit':
        print("Enjoy your movie")
        break
    elif int(user_age) < 3:
        print("Free for ages under 3")
    elif int(user_age) <= 12:
        print("Ticket cost is $10")
    else:
        print("Ticket cost is $15")

# 7-7
