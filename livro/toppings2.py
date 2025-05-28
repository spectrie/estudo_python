requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry, we are out of green peppers right now.")
    else:
        print(f'adding {requested_topping}')

print("\n Finished making your pizza!")