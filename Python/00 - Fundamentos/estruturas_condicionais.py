MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar CNH.")
else:
  print("Menor de idade, não pode tirar CNH.")


if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
  print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
  print("Menor de idade, não pode tirar CNH.")

#If Ternário
status = "Sucesso" if idade >= MAIOR_IDADE else "Falha"

print (f"{status} ao informar a idade.")