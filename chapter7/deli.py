sandwich_orders = ['pastrami', 'cheese corn', 'paneer', 'pastrami', 'veggie overloaded', 'chicken', 'pastrami']
finished_sandwiches = []

# removing pastrami from the list
print("Ran out of Pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# making sandwiches
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich")

    finished_sandwiches.append(current_sandwich)

print("\nCompleted the following orders: ")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} sandwich")