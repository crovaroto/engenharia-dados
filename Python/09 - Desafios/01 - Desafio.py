menu = """

\n***************** Opções disponíveis ****************** 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

>= """

saldo = 0
limite =  500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
operacoes = 0

while True:
  opcao = input(menu)

  if opcao == "d":
    valorDeposito = float(input("Informe o valor do depósito => "))

    if valorDeposito <= 0:
      print("Não é possível efetuar depósitos de valores menores ou iguais a 0 (zero).")
    else:
      saldo += valorDeposito
      extrato += f"Depósito: R$ {valorDeposito:.2f}\n" 
      print(f"Valor depositado R$ {valorDeposito}")
      operacoes += 1

  elif opcao == "s":
    valorSaque = float(input("Qual valor deseja sacar? => "))
    
    saldo_excedido = valorSaque > saldo
    limite_sacado = valorSaque > limite
    limite_excedido = numero_saques > LIMITE_SAQUES

    if (saldo_excedido):
      print(f"Desculpe, mas o valor o saque é maior que saldo da conta ({saldo:.2f}).")
    elif(limite_sacado):
      print("Descupe, mas o valor do saue ultrapassa o limite de saque permitido.")
    elif(limite_excedido):
      print(f"Desculpe, mas o limite de {LIMITE_SAQUES} saques(s) diários foi ultrapassado.")
    elif(valorSaque <= 0):
      print("Desculpe, mas não épossível fazer um saque do valor solicitado")
    else:
      saldo -= valorSaque
      numero_saques += 1
      extrato += f"Saque: R$ {valorSaque:.2f}\n" 
      print(f"Valor sacado R$ {valorSaque:.2f}")
      operacoes += 1

  elif opcao == "e":
    print("\n********************** Extrato **********************")
    print("Não foram realizadas operações no dia de hoje" if operacoes == 0 else extrato)
    print("*****************************************************")
    print(f"\n Saldo do dia: R$ {saldo:.2f}")
    print("*****************************************************")

  elif opcao == "s":
   print("Sair")

  elif opcao == "q":
    print("Obrigado por utilizar o nosso sistema. Até logo!")
    break 
  
  else:
    print("Operação inválida, por favor selecione novamente a opção desejada.")