def make_pizza(size, *toppings):
    """Print pizza toppings and size"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
