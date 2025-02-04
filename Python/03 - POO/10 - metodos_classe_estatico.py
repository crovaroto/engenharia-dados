class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Método de classe
    @classmethod
    def idade_nacimento(cls, ano, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    #Método estático
    @staticmethod
    def maioridade(idade):
        return idade >= 18
    
p = Pessoa.idade_nacimento(1984, "Cássio")
print(p.nome, p.idade)

print(Pessoa.maioridade(17))
print(Pessoa.maioridade(28))
