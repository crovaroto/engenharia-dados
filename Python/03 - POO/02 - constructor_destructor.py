class  Cachorro:
    def __init__(self, nome, cor, acordado=True) -> None:
        print("Iniciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Destruindo a classe...")

    def latir(self):
        print ("AU AU")

c = Cachorro("Barão", "branco e preto")
c.latir()
    
