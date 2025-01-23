import textwrap
from datetime import datetime

def menu():
  menu = """

  \n***************** Opções disponíveis ****************** 
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova conta
  [lc]\tListar contas
  [nu]\tNovo usuário
  [q]\tSair
  >= """

  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor <= 0:
        print("Não é possível efetuar depósitos de valores menores ou iguais a 0 (zero).")
  else:
    saldo += valor
    extrato += f"({datetime.now().strftime('%d/%m/%Y %H:%M')}) - Depósito: R$ {valor:.2f} \n" 
    print(f"Depósito realizado no valor de R$ {valor}")   
  
  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  saldo_excedido = valor > saldo
  limite_sacado = valor > limite
  limite_excedido = numero_saques > limite_saques

  if (saldo_excedido):
    print(f"Desculpe, mas o valor o saque é maior que saldo da conta ({saldo:.2f}).")
  elif(limite_sacado):
    print("Descupe, mas o valor do saue ultrapassa o limite de saque permitido.")
  elif(limite_excedido):
    print(f"Desculpe, mas o limite de {limite_saques} saques(s) diários foi ultrapassado.")
  elif(valor <= 0):
    print("Desculpe, mas não é possível fazer um saque do valor solicitado.")
  else:
    saldo -= valor
    numero_saques += 1
    extrato += f"({datetime.now().strftime('%d/%m/%Y %H:%M')}) - Saque de R$ {valor:.2f}\n" 
    print(f"Saque realizado no valor de R$ {valor:.2f}")

  return saldo, extrato

def exibir_extrato(saldo, operacoes, /, *, extrato):
  print("\n********************** Extrato **********************")
  print("Não foram realizadas operações no dia de hoje" if operacoes == 0 else extrato)
  print("*****************************************************")
  print(f"\n Saldo do dia: R$ {saldo:.2f}")
  print("*****************************************************")
  
  return extrato
def criar_usuario(usuarios):
  cpf = input("Informe o CPF do novo usuário (somente números) =>")
  usuario = filtrar_usuario(cpf, usuarios)
  
  if usuario:
    print("Desculpe, usuário já cadastrado com esse CPF.")
    return
  
  nome = input("Informe seu nome completo =>")
  data_nascimento = input("Informe sua data de nascimento (dd-mm-yyyy) =>")
  endereco = input("Informe seu endereço completo (logradouro, número - bairro - cidade/UF) =>")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
  print("Usuário cadastrado com sucesso.")

def filtrar_usuario(cpf, usuarios) :
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_contas(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário (somente números) =>")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Conta criada com sucesso.")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
  
  print("Desculpe, mas o usuário não foi encontrado.")

def listar_contas(contas):
  if contas == []:
    print("Ainda não há contas criadas para serem listadas.")
    return
  else:
    for conta in contas:
      linha = f"""
             Agência:\t{conta['agencia']}
             C/C:\t{conta['numero_conta']}
             Titular:\t{conta['usuario']['nome']}  
             """
      print("=" * 100)
      print(textwrap.dedent(linha))

def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo = 0
  limite =  500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []
  operacoes = 0
  numero_conta = 1

  while True:
    opcao = menu()

    if opcao == "d":
      valor = float(input("Informe o valor do depósito => "))

      saldo, extrato = depositar(saldo, valor, extrato)
      operacoes += 1
  
    elif opcao == "s":
      valor = float(input("Qual valor deseja sacar? => "))

      saldo, extrato = sacar(saldo=saldo,
                             valor=valor,
                             extrato=extrato,
                             limite=limite,
                             numero_saques=numero_saques,
                             limite_saques=LIMITE_SAQUES)
      operacoes += 1
      
    elif opcao == "e":
      exibir_extrato(saldo, operacoes, extrato=extrato)
    
    elif opcao == "nu":
      criar_usuario(usuarios)

    elif opcao == "nc":
      conta = criar_contas(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)
        numero_conta += 1

    elif opcao == "lc":
      listar_contas(contas) 
    
    elif opcao == "q":
      print("Obrigado por utilizar o nosso sistema. Até logo!")
      break 

    else:
      print("Operação inválida, por favor selecione novamente a opção desejada.")

main()