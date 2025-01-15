#Versão 1 
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
quadrado= []

for numero in numeros:
  if (numero % 2 == 0):
    pares.append(numero)

for numero in numeros:
  quadrado.append(numero ** 2)

print(pares)
print(quadrado)

#Versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero %2 == 0]
quadrado = [numero ** 2 for numero in numeros]

print(pares)
print(quadrado) 
