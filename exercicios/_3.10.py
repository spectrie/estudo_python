listaDeCoisas = ['league of legens', 'gta', 'mario kart', 'overwatch', 'call of duty', 'path of exile 2' ]

listaDeCoisas.append('dying light')
print(listaDeCoisas)
listaDeCoisas.insert(1, 'the witcher 3')

del listaDeCoisas[3]

popped_list = listaDeCoisas.pop(-2)

print(listaDeCoisas)

listaDeCoisas.remove('gta')
print(listaDeCoisas)

listaDeCoisas.sort()
print(listaDeCoisas)

listaDeCoisas.sort(reverse=True)
print(listaDeCoisas)
print("@")
print(sorted(listaDeCoisas))
print(listaDeCoisas)


listaDeCoisas.reverse()
print(listaDeCoisas)

print(len(listaDeCoisas))

print(sorted(listaDeCoisas, reverse=True))