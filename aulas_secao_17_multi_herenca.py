"""
Herença multipla

Herança multipla nada mais é a posibilidade que uma classe herde tudo de mais de uma classe.

A herança multipla pode ser feia de duas maneiras:
    - Por multiderivação direta
    - Multiderivação indireta

"""


class SerVivo:

    def __init__(self, ser):
        self.__vida = True
        self.__ser = ser

    def vida_existente(self):
        if self._SerVivo__vida is True:
            return f'O {self._SerVivo__ser} é vivo.'
        else:
            return f'O {self._SerVivo__ser} não é vivo.'


class Animal(SerVivo):

    def __init__(self, ser, tipo, especie):
        super().__init__(ser)
        self.__tipo = tipo
        self.__especie = especie

    def definicao(self):
        return f'Eu sou o(a) {self._SerVivo__ser} um(a) {self._Animal__especie} sou Animal.'


class Aquatico(Animal):

    def __init__(self, ser, tipo, especie):
        super().__init__(ser, tipo, especie)

    def nada(self):
        return f'O(A) {self._SerVivo__ser} da espécie {self._Animal__especie} está nadando'

    def definicao(self):
        return f'Eu sou o(a) {self._SerVivo__ser} um(a) {self._Animal__especie} sou Aquatico.'


class Terrestre(Animal):

    def __init__(self, ser, tipo, especie,):
        super().__init__(ser, tipo, especie)

    def andar(self):
        return f'O(A) {self._SerVivo__ser} da espécie {self._Animal__especie} está andando'

    def definicao(self):
        return f'Eu sou o(a) {self._SerVivo__ser} um(a) {self._Animal__especie} sou Terrestre.'


class Reptil(Terrestre, Aquatico):

    def __init__(self, ser, tipo, especie):
        super().__init__(ser, tipo, especie)


peixe = Aquatico('Nemo', 'Vertebrado', 'Peixe')
print(peixe.vida_existente())
print(peixe.nada())
print(peixe.definicao())

gato = Terrestre('Fifi', 'Vertebrado', 'Gato')
print(gato.vida_existente())
print(gato.andar())
print(gato.definicao())

cobra = Reptil('Alfredo', 'Vertebrado', 'Cobra')
print(cobra.vida_existente())
print(cobra.andar())
print(cobra.nada())
print(cobra.definicao()) # Method Resolution Order - MRO

