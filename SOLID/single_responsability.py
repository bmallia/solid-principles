
##jeito errado
class Quadrado:

    def __init__(self, comprimento_lado=0) -> None:
        self.comprimento_lado = comprimento_lado

    def calcula_area(self):
        return self.comprimento_lado ** 2

    def desenhar(self):
        ##desenha um quadrado
        pass

##qual é o problema dessa abordagem?
## ela não está errada, mas podemos dividir em 2 classes, cada uma com a sua responsabilidade

class CalcularQuadrado:

    def __init__(self, comprimento_lado=0) -> None:
        pass

    def calcular_area(self)          :
        ##desenha um quadrado
        pass

class DesenhaQuadrado:

    def desenhar(self):
        pass