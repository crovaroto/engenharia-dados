#Criação de Função

#1. Função inicial
def saudacao():
    print('Hello World!')

saudacao()

#2. Função com parâmetro
def saudacaoP(nome):
    print(f'Olá, {nome}!')
    
saudacaoP('Cássio')

#3. Função com parâmetreo default
def saudacaoPD(nome, curso = 'Python'):
    print(f'Olá, {nome}! Bem-vindo ao curso de {curso}')
    
saudacaoPD('Cássio')

#4. Função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(1,2)
print(f'O resultado é: {resultado}')