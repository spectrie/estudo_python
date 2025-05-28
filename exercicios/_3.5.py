peoples =['Marcello', 'Simone', 'Tito', 'Láysa']

print(f"{peoples[0].title()}, gostária de vim jantar?")
print(f"{peoples[1].title()}, gostária de vim jantar?")
print(f"{peoples[2].title()}, gostária de vim jantar?")
print(f"{peoples[3].title()}, gostária de vim jantar?")

print(f"O {peoples[0]} não virá ao jantar.")

peoples[0] = 'Ramon'
print(f"{peoples[0].title()}, gostária de vim jantar?")

print("\nEncontrei uma mesa maior, então irei convidar mais pessoas para o jantar")

peoples.insert(0, 'João')
peoples.insert(2, 'Isabella')
peoples.append('Thiago')

print(f"\n{peoples[0].title()}, gostária de vim jantar?")
print(f"{peoples[1].title()}, gostária de vim jantar?")
print(f"{peoples[2].title()}, gostária de vim jantar?")
print(f"{peoples[3].title()}, gostária de vim jantar?")
print(f"{peoples[4].title()}, gostária de vim jantar?")
print(f"{peoples[5].title()}, gostária de vim jantar?")
print(f"{peoples[-1].title()}, gostária de vim jantar?")

print("\nA mesa não chegará a tempo, só posso convidar duas pessoas para o jantar.")

convidado0=peoples.pop(0)
print(f"{convidado0}, Lamento não poder lhe convidar.")

convidado1 = peoples.pop(0)
print(f"{convidado1}, Lamento não poder lhe convidar.")

convidado2 = peoples.pop(0)
print(f"{convidado2}, Lamento não poder lhe convidar.")

convidado3 = peoples.pop(0)
print(f"{convidado3}, Lamento não poder lhe convidar.")

convidado4 = peoples.pop(0)
print(f"{convidado4}, Lamento não poder lhe convidar.")

print(f"\n{peoples[-1]}, ainda está convidado")
print(f"{peoples[-2]}, ainda está convidada")

del peoples[0]
del peoples[0]

print(peoples)