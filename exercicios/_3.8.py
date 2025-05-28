locais_conhecer = ['Estados Unidos', 'Italia', 'Japao', 'Franca', 'Holanda']
print(locais_conhecer)

print("\nLista em ordem alfabetica:")
print(sorted(locais_conhecer))

print("\nLista original:")
print(locais_conhecer)

print("\nLista em ordem alfabetica reversa:")
print(sorted(locais_conhecer, reverse=True))

print("\nLista original:")
print(locais_conhecer)

print("\nLista original porém invertida permanentemente:")
locais_conhecer.reverse()
print(locais_conhecer)

print("\nLista original de volta a forma original:")
locais_conhecer.reverse()
print(locais_conhecer)

print("\nLista original em ordem alfabetica de forma permanente:")
locais_conhecer.sort()
print(locais_conhecer)

print("\nLista original em ordem alfabetica inversa de forma permanente:")
locais_conhecer.sort(reverse=True)
print(locais_conhecer)
