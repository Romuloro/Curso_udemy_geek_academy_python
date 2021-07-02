"""
Herança - (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança a partir de uma classe existente, nós extendemos outra classe que
passa a herdar atributos e métodos da classe herdada.

Quando a classe herda de outra ela tem todos os atributos e métodos da outra classe

Quando uma classe herda de uma classe, a classe herdada é conhecida como:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;

Quando uma classe herda de uma classe ela é chamada por:
    - Subclasse
    - Classe filha.

Sobrescrita de Métodos (Overriding) - Ocorre quando reimplementamos um método na classe
filha.

"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self,nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome,cpf)
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self._Pessoa__nome} Funcionário: {self.__matricula}'


cl1 = Cliente('Rômulo', 'Rodrigues', '14275478932', 7000)
fun = Funcionario('Rodrigo', 'Ribeiro', '78177496314', '874126-4')

print(cl1.nome_completo())
print(fun.nome_completo())

# Sobrescrita de Métodos (Overriding)


