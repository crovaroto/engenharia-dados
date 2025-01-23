#for
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end="")
  
print()  


#For .. Else
for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end="")
  
else:
  print()
  print("Fim da execução")

#Função RANGE
#list(range(4))
#Ex. utilizando RANGE no for
for numero in range(0, 51, 5):
  print(numero, end=" ")

#WHILE
opcao = -1

while opcao != 0:
  opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n :"))

  if opcao == 1:
    print("Sacando... ")
  elif opcao == 2:
    print("Exibindo extrato... ")
  else:
    print("Obrigado por usar nosso sistema.")

#BREAK
while opcao != 0:
  opcao = int(input("Informe um número :"))

  if opcao == 10:
    break

  print(opcao, end=" ")

#Ex.

