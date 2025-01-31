class Bibicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim...")

    def parar(self):
        print("parando....")

    def correr(self):
        print("Correndo.....")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
b1 = Bibicleta("vermelha", "caloi", 2025, 600)
b1.buzinar() # equivalente a Bicicleta.buzinar(b1)
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1.__str__())

#Self (representação do objeto) é sempre o primeiro parâmetro