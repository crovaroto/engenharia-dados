#Sintaxe
#class A:
#    pass

#class B:
#   pass

#class C(A, B):
#    pass 

class Animal:
    def __init__(self, num_patas) -> None:
        self.num_patas = num_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw) -> None:
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw) -> None:
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    pass 


cachorro = Cachorro(num_patas=4, cor_pelo="Preto")
print(cachorro)

print("---------------------------------------")

ornitorrinco = Ornitorrinco(num_patas=4, cor_pelo="Marrom", cor_bico="Laranja")
print(ornitorrinco)