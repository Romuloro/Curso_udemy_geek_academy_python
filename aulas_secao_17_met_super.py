"""
Método Super

Se refere a super classe (classe mãe)

"""

class Animal:

    def __init__(self, tipo, especie):
        self.__tipo = tipo
        self.__especie = especie

    def faz_som(self, som=None):
        if som is None:
            print(f'O {self.__especie} não emite som')
        else:
            print(f'O {self.__especie} {som}')



class Formiga(Animal):

    def __init__(self, tipo, especie, categoria):
        super().__init__(tipo, especie)
        self.__categoria = categoria


class Humano(Animal):

    def __init__(self, tipo, especie, etnia):
        super().__init__(tipo, especie)
        self.__etnia = etnia


julio = Humano('Mamífero', 'Humano', 'negro')
formiga_1 = Formiga('Inseto', 'Formiga', 'cortadeira')

julio.faz_som('Fala')
formiga_1.faz_som()

