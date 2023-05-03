class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def getTipo(self):
        return self.tipo

    def ligar(self):
        print(f'Ligando seu {self.getTipo()}...')


class Carro(Veiculo):
    def __init__(self, statusCapo):
        tipo = input("Digite o tipo do veículo: ")
        super().__init__(tipo)
        self.statusCapo = statusCapo
        
    def getStatusCapo(self):
        return print(f'O capô do seu {self.getTipo()} está {self.statusCapo} !!!')
    
    def setStatusCapo(self, novoStatus):
        self.statusCapo = novoStatus
        
class Moto(Veiculo):
    def __init__(self, possuiBau):
        tipo = input("Digite o tipo do veículo: ")
        super().__init__(tipo)
        self.possuiBau = possuiBau
        
    def getStatusBau(self):
        return print(f'A sua {self.getTipo()} possui bau? {self.possuiBau} !!!')
    
    def setStatusBau(self, novoStatusBau):
        self.possuiBau = novoStatusBau
        

motoca = Moto("Não")
#motoca.ligar()
#motoca.getTipo()
#motoca.getStatusBau()
#motoca.setStatusBau("Sim")
#motoca.getStatusBau()

meuCarro = Carro("Fechado")
#meuCarro.ligar()
#meuCarro.getTipo()
#meuCarro.getStatusCapo()
#meuCarro.setStatusCapo("Aberto")
#meuCarro.getStatusCapo()