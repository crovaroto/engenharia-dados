#Sintaxe
#class A:
#    pass

#class B(A):
#    pass

class Veiculo:
    def __init__(self, cor, placa, num_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print("Ligando motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Estou ' if self.carregado else 'Não estou '} carregado")

moto = Motocicleta("vermelha", "ABC123", 2)
moto.ligar_motor()

carro = Carro("branco", "XYZ987", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "KLM456", 8, True)
caminhao.esta_carregado()