"""
Métodos mágicos são todos os métodos que utilizam o dunder __method__
"""

# Construtor (__init__)

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__pagina = paginas

    def __repr__(self): #__repr__ É a representasão do objeto.
        return self.__titulo

    def __str__(self): #__str__ É a string que é a representação inicial para usuário.
        return self.__titulo

    def __len__(self): #__len__ o tamanho do objeto.
        return self.__paginas


