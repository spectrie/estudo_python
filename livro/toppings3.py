requested_toppings = []

if requested_toppings: #lista vazia retorna false na verificação do if.
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?")
