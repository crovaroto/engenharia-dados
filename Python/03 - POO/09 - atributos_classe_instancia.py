class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Cássio", 1)
aluno2 = Estudante("Nicolas", 2)

mostrar_valores(aluno1, aluno2)
print("--------------------------------")

print("Alterando variável de instância:")
aluno1.matricula = 3 
mostrar_valores(aluno1, aluno2)
print("--------------------------------")

print("Alterando variável de classe:")
Estudante.escola =  'Python'
mostrar_valores(aluno1, aluno2)