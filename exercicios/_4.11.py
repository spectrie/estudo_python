pizzas = ['4 queijos', 'Frango com catupiri', 'Filé']

for pizza in pizzas:
    print(f"Gosto de pizza de {pizza}")
    print(f"pizza de {pizza} é muito gostoso \n")

print("Eu amo pizza")

friend_pizzas = pizzas[:]

pizzas.append('bacon')
friend_pizzas.append('chocolate')

print("Minhas pizzas favoritas são: ")
for pizza in pizzas:
    print(pizza)


print("\nMinhas pizzas favoritas são: ")
for pizza in friend_pizzas:
    print(pizza)