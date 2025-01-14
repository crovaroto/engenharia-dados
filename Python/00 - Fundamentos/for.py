"""for i in range(5):
    print(i)


for i in range(1, 5):
    print(i)


for i in range(1, 12, 3):
    print(i)
"""
soma = 0

for i in range(1, 4):
    nota = float(input(f"Informe a sua nota {i}: "))
    soma = soma + nota

print("A média é:", str(soma/3))