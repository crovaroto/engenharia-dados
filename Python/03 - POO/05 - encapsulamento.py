class Conta:
#Conceito de privado é conter "_" no nome, mas tudo no python é considerado público
    def __init__(self, saldo=0) -> None:
        self._saldo  = saldo # _saldo é conceituado como privado

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    # Exemplo de acessar atributos privados
    def mostrar_saldo(self):
        return self._saldo


conta = Conta(100)