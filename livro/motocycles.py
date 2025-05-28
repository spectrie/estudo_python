"""motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#alteração do primeiro elemento da lista:
motorcycles[0] = 'ducati' 
print(motorcycles)
#adição do elemento honda ao final da lista através do método append()
motorcycles.append('honda')
print(motorcycles)


motorcycles2 = []

motorcycles2.append('honda')
motorcycles2.append("yamaha")
motorcycles2.append('suzuki')
print(motorcycles2)

#O método inset() insere um valor na posição informada como parametro juntamente com o valor a ser inserido.
motorcycles.insert(0, 'bmw')
print(motorcycles)

#a função del remove o item informado caso saiba a posição como no exemplo abaixo:
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
"""
#esse método remove o ultimo elemento da lista mas não o deleta, permitindo que vc armazene dentro de outra váriavel.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()

print(f"A ultima moto que vc comprou foi: {last_owned.title()}")
"""

"""
first_owned = motorcycles.pop(0)
print(f"A primeira moto que eu comprei foi a {first_owned.title()}")

#Usa-se o del caso nunca mais vá usar o elemento removido da lista
#Usa-se o pop() caso o elemento removido da lista ainda seja usado em outro local posteriormente.
print(motorcycles)

#remoção de um elemento através do valor utilizando o método remove() e passando o valor a ser removido como argumento para o método
motorcycles.remove('yamaha')
print(motorcycles)
"""

#é possivel armazenar o valor que vai ser removido dentro de uma váriavel com o fim de justificar a remoção do item.
too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} é muito cara para mim")