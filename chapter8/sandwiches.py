def sandwich_toppings(*toppings):
    """Print sandwich toppings"""
    print("\nThe following toppings are being added to your sandwich: ")
    for topping in toppings:
        print(f"-{topping}")


sandwich_toppings('lettuce', 'tomato', 'onion')
sandwich_toppings('onion', 'corn', 'cheese', 'lettuce')