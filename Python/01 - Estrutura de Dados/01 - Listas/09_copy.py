lista = []

lista.append(1)
lista.append("Dois")
lista.append([3, 4, 5])

lista_copia = lista.copy()
lista_copia[0] = 99
lista_copia.append("Nova Lista")

print(lista)
print(lista_copia)