'''
    A principal idéia é que a classe mãe deve ser genérica e abstrata para ser estendida e
    reaproveitada por classes filhar. Esse prinício rege que a classe mãe não deve ser alterada


    No PYthon, podemos fazer uma operação conhecida como Monkey-Patching.
    Uma classe em Python é mutável e uma método é apenas um atributo de uma classe. Dessa forma 
    é possível sobrescrever um método dinamicamente em tempo de execução. 
'''
from single_responsability import CalcularQuadrado



if __name__ == "__main__":
    area = CalcularQuadrado(10)

    def forma_geometrica():
        return 'Sou um quadrado'

    area.forma_geometrica = forma_geometrica

    print(area.forma_geometrica())