#Listas

notas = [7.0, 10.0, 5.5]

#Criando listas
lista = [] #vazia
lista1 = list()

#Indexação 
lista = [10, 'Cássio', 3.1415, True]

print(lista[0])
print(lista[-1]) #o último, negativa vai de trás para frente

#Slices
lista = [10, 50, 30, 20, 90]
print(lista[0:3])
#print(lista[0:3:2]) #:2 = pular de 2 em 2

#Integração com FOR

#1.
for i in lista:
    print(i)

#2.
print('Comprimento da lista: ', len(lista))
for i in range(len(lista)):
    print(lista[i])