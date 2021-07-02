"""
Representam os comportamentos do objeto (as suas ações).

Os métodos são dividios em:
    Métodos de Instâncias precisa ser ligado ao objeto para ser utilizado
    Métodos de Classe

O método __init__ é p construtor, que construe o objeto a partir da classe.

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligado = False

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}')


uss1 = Usuario('Élissa', 'Santos Oliveira', 'elissa@gmail.com', 12245)

print(uss1.nome_completo())

