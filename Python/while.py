numero_sorteado = 15

numero_escohido = int(input('Informe um número inteiro entre 1 e 20: '))

while int(numero_sorteado) != numero_escohido:
    numero_escohido = int(input('Você errou! Informe outro número  inteiro entre 1 e 20: '))   

input('Você acertou!')


contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1