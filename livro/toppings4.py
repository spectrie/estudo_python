avaiable_toppings = ['mushrooms', 'olives', 'green peppers',
                    'peperoni', 'pinneaple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping in avaiable_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")


print("\nFinished making your pizza")