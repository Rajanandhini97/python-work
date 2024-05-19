# adding numbers

while True:
    print("\nEnter two numbers to add. (Type 'q' to quit)")
    first_num = input("Enter first number: ")
    if first_num == 'q':
        break
    second_num = input("Enter second number: ")
    if second_num == 'q':
        break
    try:
        total = int(first_num) + int(second_num)
    except ValueError:
        print("\nPlease provide a valid number")
    else:
        print(f"Your total is {total}")
