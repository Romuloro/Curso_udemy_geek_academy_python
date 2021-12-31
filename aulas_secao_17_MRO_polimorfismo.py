"""
Method Resolution Order (MRO)

MRO é a ordem de execução dos métodos, ou seja quem será executado primeiro.
MRO tem 3 formas:
    - Via propriedade da clase
    - Via método MRO()
    - Via help

Polimorfismo - Objetos que podem se comportar de diferentes formas
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} esta comendo')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.__nome} fala wau wau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.__nome} fala miau maiu')


class Formiga(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.__nome} fala algo')