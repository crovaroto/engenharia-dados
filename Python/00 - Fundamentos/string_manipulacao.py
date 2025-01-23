curso = " pYthon "

print(curso.upper())

print(curso.lower())

print(curso.title())

print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())

print(curso.center(10, "#"))

print(".".join(curso))


#Interpolação de variáveis

nome = "Cassio"
idade = 40
profissao = "Analista"
linguagem = "Python"

dados = {"nome": "Cassio", "idade":40}

#%
print("Nome: %s, Idade: %d" %(nome, idade))

#format
print("Nome: {}, Idade: {}".format(nome, idade))
print("Nome: {0}, Idade: {1}".format(nome, idade))
print("Nome: {nome}, Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome}, Idade: {idade}".format(**dados))

#f-String
print(f"Nome: {nome}, Idade: {idade}")


#Fatiamento de string
nome = "Cassio Rovaroto"

print(nome[0])

print(nome[:9])

print(nome[10:])

print(nome[10:16])

print(nome[10:16:2])

print(nome[:])

print(nome[::-1])

#String triplas
nome =  "Cassio"

mensagem =  f"""
Olá me chamo {nome}.
Estou aprendendo Python.
    Essa mensagem tem diferentes recuos 
"""

print(mensagem)