class Pessoa:
    def __init__(self, nome, ano_nascimento) -> None:
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual =  2025
        return _ano_atual - self._ano_nascimento 

pessoa = Pessoa("Cassio", 1984)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")       