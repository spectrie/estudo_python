cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
#método que ordena em ordem alfabetica
cars.sort()
print(cars)
#o parametro inverte a ordem alfabetica.
cars.sort(reverse=True)
print(cars)

cars2 = ['mercedes', 'chevrolet', 'fiat', 'nissan']

print("aqui está a lista original:")
print(cars2)

print("aqui esta a lista com sorted:")
print(sorted(cars2))

print("aqui está a lista original novamente")
print(cars2)

cars2.reverse()
print(cars2)

cars2.reverse()
print(cars2)

