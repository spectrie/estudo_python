players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#se ommitir o primeiro indice, o python pegará a lista do começo
#se omitir o segundo incide, o python entregara toda a lista a partir do indice informado.

print("here are the first three player on my team: ")
for player in players[:3]:
    print(player.title())