class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
        
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_voo(obj):
    obj.voar()    

plano_voo(Pardal())
plano_voo(Avestruz())