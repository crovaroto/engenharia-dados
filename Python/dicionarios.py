#Dicionários

#Criação
dicionario = {}
dicionario = dict()

dicionario = {
    'nome': 'Cássio',
    'idade': 39,
    'altura': 1.78
}

print(dicionario)
print(dicionario['nome'])

#Adicionar elementos
dicionario['programador'] =  True

print(dicionario)
print(dicionario['programador'])


# Iterar sobre dicionário

for i in dicionario:
    print(i) #Chave

for i in dicionario:
    print(dicionario[i]) #Valor

# Testando a existência em um dicionário
print('peso' in dicionario)
print('altura' in dicionario)