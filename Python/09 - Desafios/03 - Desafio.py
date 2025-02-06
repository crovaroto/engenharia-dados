from abc import ABC, abstractstaticmethod, abstractproperty
import textwrap
from datetime import datetime

class Cliente:
  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []

  def realizarTransacoes(self, conta, transacao):
    transacao.registrar(conta)

  def adicionarConta(self, conta):
    self.contas.append(conta)


class PessoaFisica(Cliente):
  def __init__(self, nome, data_nascimento, cpf, endereco):
    super().__init__(endereco)
    self.nome = nome
    self.data_nasicmento =  data_nascimento
    self.cpf = cpf

class Conta:
  def __init__(self, saldo, numero, cliente):
    self.saldo = saldo
    self.numero = numero
    self.agencia = "0001"
    self.cliente = cliente
    self.historico = Historico()

  @classmethod
  def novaConta(cls, cliente, numero):
    return cls(numero, cliente)
  
  @property
  def saldo(self):
    return self._saldo
  
  @property
  def numero(self):
    return self._numero
  
  @property
  def agencia(self):
    return self._agencia
  
  @property
  def cliente(self):
    return self._cliente
  
  @property
  def historico(self):
    return self._historico
  
  def sacar(self, valor):
    saldo = self.saldo
    saldo_excedido = valor > saldo
    
    if (saldo_excedido):
      print(f"Desculpe, mas o valor o saque é maior que saldo da conta ({saldo:.2f}).")
    elif (valor > 0):
      saldo -= valor
      print(f"Saque realizado no valor de R$ {valor:.2f}")
      return True
    else:
      print("Não possível realizar a operação. Verifique o valor a sacar.")

    return False
  
  def depositar(self, valor):
    if valor <= 0:
      print("Não é possível efetuar depósitos de valores menores ou iguais a 0 (zero).")
      return False
    else:
      self._saldo += valor
      print(f"Depósito realizado no valor de R$ {valor}")   
      
    return True


class ContaCorrente(Conta):
  def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
    super().__init__(numero, cliente)
    self.limite = limite
    self.limite_saques =  limite_saques

  def sacar(self, valor):
    numero_saques = len([transacao for transacao in self.historico.transacoes if 
                         transacao["tipo"] == Saque.__name__])
    limite_excedido = valor > self.limite
    saques_excedidos = numero_saques >= self.limite_saques

    if (limite_excedido):
      print(f"O valor é maior que o limite para operações.")
    elif saques_excedidos:
      print(f"Este numero de saque no peŕido ({saques_excedidos}) é maior que limite ({self.limite_saques})")
    else:
      return super().sacar(valor)

    return False
  
  def __str__(self):
    return f"""\
            Agência:\t{self.agencia}
            C/C:\t{self.numero}
            Titular:\t{self.cliente.nome}
    """

class Historico:
  def __init__(self):
    self._transacoes = []

  @property
  def transacoes(self):
    return self._transacoes
  
  def adicionarTransacao(self, transacao):
    self._transacoes.append(
      {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor,
        "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
      }
    )

class Transacao(ABC):
  @property
  @abstractproperty
  def valor(self):
    pass

  @abstractstaticmethod
  def registrar(self, conta):
    pass 

class Saque(Transacao):
  def __init__(self, valor):
    self._valor = valor

    @property
    def valor(self):
      return self._valor
    
    def registrar(self, conta):
      sucessoTransacao = conta.sacar(self.valor)

      if (sucessoTransacao):
        conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = valor

    @property
    def valor(self):
      return self._valor
    
    def registrar(self, conta):
      sucessoTransacao = conta.depositar(self.valor)

      if (sucessoTransacao):
        conta.historico.adicionar_transacao(self)

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

def exibir_extrato(clientes):
  cpf = input("Informe seu CPF , por favor: ")
  cliente = filtrar_usuario(cpf, clientes)
  
  if not (cliente):
    print("Cliente não foi encontrado.")
    return

  conta =  recuperarContaCliente(cliente)

  if not (conta):
    return
  

  print("\n********************** Extrato **********************")
  transacoes = conta.historico.transacoes

  extrato = ""

  if not (transacoes):
    extrato = print("Não foram realizadas operações no dia de hoje")
  else:
    for transacao in transacoes:
      extrato += f"\n{transacao['tipo']}: \n\tR$ {transacao['valor']:.2f}"

  print(extrato)    
  print("*****************************************************")
  print(f"\n Saldo do dia: R$ {conta.saldo:.2f}")
  print("*****************************************************")
  
def criar_usuario(usuarios):
  cpf = input("Informe o CPF do novo usuário (somente números) =>")
  usuario = filtrar_usuario(cpf, usuarios)
  
  if usuario:
    print("Desculpe, usuário já cadastrado com esse CPF.")
    return
  
  nome = input("Informe seu nome completo =>")
  data_nascimento = input("Informe sua data de nascimento (dd-mm-yyyy) =>")
  endereco = input("Informe seu endereço completo (logradouro, número - bairro - cidade/UF) =>")

  usuario = PessoaFisica(nome=nome, data_nascimento=data_nascimento, endereco=endereco)
  usuarios.append(usuario)

  print("Usuário cadastrado com sucesso.")

def filtrar_usuario(cpf, usuarios) :
  usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf ]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_contas(numero_conta, usuarios, contas):
  cpf = input("Informe o CPF do usuário (somente números) =>")
  usuario = filtrar_usuario(cpf, usuarios)

  if not (usuario):
    print("Cliente não encontrado.")
    return

  conta = ContaCorrente.novaConta(cliente=usuario, numero=numero_conta)
  contas.append(conta)
  usuarios.contas.append(conta)

  print("Conta criada com sucesso.")

def listar_contas(contas):
  for conta in contas:
    print("=" * 100)
    print(textwrap.dedent(str(conta)))

def recuperarContaCliente(cliente):
  if not (cliente.contas):
    print("Este cliente não possui conta")
    return
  
  return cliente.contas[0]

def depositar(clientes):
  cpf = input("Informe seu CPF, por favor: ")
  cliente = filtrar_usuario(cpf, clientes)

  if not (cliente):
    print("Cliente não encontrado.")
    return
  
  valor = float(input("Informe o valor a ser depositado: "))
  transacao = Deposito(valor)

  conta = recuperarContaCliente(cliente)
  if not (conta):
    return
  
  cliente.realizarTransacao(conta, transacao)

def sacar(clientes):
  cpf =  input("Informe seu CPF, por favor: ")
  cliente = filtrar_usuario(cpf, clientes)

  if not (cliente):
    print("Cliente não foi encontrado.")
    return
  
  valor = float(input("Informe o valor do saque: "))
  transacao = Saque(valor)

  conta = recuperarContaCliente(cliente)
  if not (conta):
    return
  
  cliente.realizarTransacao(conta, transacao)

def main():
  clientes = []
  contas = []

  while True:
    opcao = menu()

    if opcao == "d":
      depositar(clientes)

    elif opcao == "s":
      sacar(clientes)
      
    elif opcao == "e":
      exibir_extrato(clientes)
    
    elif opcao == "nu":
      criar_usuario(clientes)

    elif opcao == "nc":
      numero_conta  = len(contas) + 1
      criar_contas(numero_conta, clientes, contas)

    elif opcao == "lc":
      listar_contas(contas) 
    
    elif opcao == "q":
      print("Obrigado por utilizar o nosso sistema. Até logo!")
      break 

    else:
      print("Operação inválida, por favor selecione novamente a opção desejada.")

main()